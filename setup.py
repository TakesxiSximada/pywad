#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

ROOT = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(ROOT, 'README')

try:
    with open(README_PATH, 'rb') as fp:
        long_desc = fp.read()
except:
    long_desc = ''

requires = ['selenium>=2.35']

setup(
    name='pywad',
    version='0.1.3',
    url='https://github.com/TakesxiSximada/pywad',
    download_url='https://github.com/TakesxiSximada/pywad/archive/master.zip',
    license='BSD',
    author='TakesxiSximada',
    author_email='takesxi.sximada@gmail.com',
    description='The Python Web Auto Drive framework using selenium.webdriver.',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment :: Mozilla',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        ],
    platforms='any',
    include_package_data=True,
    install_requires=requires,
    packages=find_packages(),
    )
