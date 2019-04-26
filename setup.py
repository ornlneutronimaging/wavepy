#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# what packages are required for this module to be executed
REQUIRED = ['scipy',
            'tqdm',
            'easygui_qt',
            'xraylib',
            'dxchange',
            'configparser',
            'matplotlib',
            'numpy',
            'h5py',
            'pyfftw',
            ]

setup(
    name='wavepy',
    author='Walan Grizolli',
    packages=find_packages(),
    version=open('VERSION').read().strip(),
    description = 'X-ray and neutron interferometry.',
    license='BSD-3',
    platforms='Any',
    install_requires=REQUIRED,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: BSD-3',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
