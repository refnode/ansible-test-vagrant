# Copyright 2015 refnode
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# import std libs
import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'lib'))
# import third party libs
from setuptools import setup, find_packages
# import local libs
from ansibletestvagrant import meta


install_requires = [
    "setuptools >= 0.7.0",
    "ansible >= 0.7.0",
]

setup(
    name=meta.__title__,
    version=meta.__version__,
    description=meta.__summary__,
    long_description=open('README.rst').read(),
    license=meta.__license__,
    url=meta.__uri__,
    author=meta.__author__,
    author_email=meta.__email__,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    keywords='',
    package_dir={ '': 'lib' },
    packages=find_packages('lib'),
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "ansible-test-vagrant=ansibletestvagrant.shell:main",
        ],
    }
)
