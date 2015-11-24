#!/usr/bin/env python
# Copyright (c) 2015 refnode and contributors

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# import std libs
import os
import subprocess
import shutil
# import third party libs
import yaml
# import local libs


VAGRANT_CONFIG="""
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box_check_update = false
  # Workaround for GH-4675
  config.vm.synced_folder ".", "/vagrant"
  config.vm.box = "%(vagrant_box)s"
  config.vm.provider :virtualbox do |vb|
    vb.gui = true
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--memory", 2048]
    vb.customize ["modifyvm", :id, "--ioapic", "on"]
    vb.customize ["modifyvm", :id, "--cpus"  , 1]
  end
  config.vm.define "%(role_name)s.example.com", primary: true do |nodeconfig|
    nodeconfig.vm.host_name = "%(role_name)s.example.com"
  end
end
"""


role_dir          = os.path.basename(os.getcwd())
role_name         = role_dir.split('-')[2]
vagrant_file_dir  = os.path.join(os.getcwd(), 'spec')
vagrant_file_path = os.path.join(vagrant_file_dir, 'Vagrantfile')
vagrant_env = os.environ
vagrant_env["VAGRANT_CWD"] = os.path.dirname(vagrant_file_path)


def parse_vagrant_ssh_config(data):
    lines = data.split('\n')
    lines = [line.strip() for line in lines if line != '']
#    params = ['HostName', 'User', 'Port', 'UserKnownHostsFile', 'StrictHostKeyChecking',
#              'PasswordAuthentication', 'IdentityFile', 'IdentitiesOnly', 'LogLevel']
    ssh_params = {}
    for line in lines:
        k,v = line.split(' ')
        ssh_params[k.lower()] = v
    return ssh_params

def environ_setup():
    environ_name = os.environ.get('ANSIBLE_TEST_VAGRANT_ENV', 'default')
    if not environ_name.endswith('.yml'):
        environ_name += '.yml'
    configfile = os.path.join(os.getcwd(), 'spec', 'acceptance', 'nodesets', environ_name)
    if not os.path.isfile(configfile):
        raise IOError('Environment config file not found: %s' % configfile)
    config = yaml.load(open(configfile))

    os_release = config['HOSTS'].keys()[0]
    vagrant_box = config['HOSTS'][os_release]['box']

    vagrant_config = {
        'vagrant_box': vagrant_box,
        'role_name': role_name,
    }
    print vagrant_config
    vagrant_config_data = VAGRANT_CONFIG % vagrant_config
    if os.path.isfile(vagrant_file_path):
        os.unlink(vagrant_file_path)
    with open(vagrant_file_path, 'wb') as fh:
        fh.write(vagrant_config_data)
    subprocess.check_call(['vagrant', 'up'], env=vagrant_env)
    ssh_config = subprocess.check_output(['vagrant', 'ssh-config'], env=vagrant_env)
    return parse_vagrant_ssh_config(ssh_config)

def test_run(config):
    pass

def environ_teardown():
    subprocess.check_call(['vagrant', 'destroy', '-f'], env=vagrant_env)
    shutil.rmtree(os.path.join(vagrant_file_dir, '.vagrant'))
    os.unlink(vagrant_file_path)

def main():
    ssh_config = environ_setup()
    test_run(ssh_config)
    environ_teardown()


if __name__ == '__main__':
    main()
