#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Based on [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

import os
import re
import setuptools

def get_version():
    # Regular expression to capture version number
    # Tested in https://regexr.com/
    REG_VERSION = re.compile(r'\b(__version__\s*=\s*[\'"])([.0-9]*)(["\'])')

    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'jupyterbookmaker/jupyterbookmaker.py')) as f:
        for line in f:
            if REG_VERSION.match(line):
                return REG_VERSION.match(line).group(2)
    raise RuntimeError('No version info found.') 

setuptools.setup(
    name='jupyterbookmaker',
    version=get_version(),
    author='Ricardo M. S. Rosa',
    author_email='rmsrosa@gmail.com',
    description='Adds book-like structure to a collection of jupyter notebooks',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rmsrosa/jupyterbookmaker',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
        'Operating System :: OS Independent'
    ],
    license=open('LICENSE', 'r').read()
)
