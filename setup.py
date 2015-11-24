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
