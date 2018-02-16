#!/usr/bin/env python

from distutils.core import setup

try:
    from setuptools import setup, find_packages  # noqa
except ImportError:
    from distutils.core import setup


setup(
    name='harview',
    version='0.2.2',
    description=(
        'A commandline tool which takes as input a .har (HTTP Archive) file '
        'and dumps a human-readable summary of it to the console'
    ),
    long_description='',
    license='GPLv3',
    author='Ferry Boender',
    author_email='ferry.boender@gmail.com',
    url='https://github.com/fboender/harview',
    scripts=[
        'src/harview',
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
