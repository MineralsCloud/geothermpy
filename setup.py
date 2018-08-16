#!/usr/bin/env python

from setuptools import setup

setup(
    name='geothermpy',
    version='0.0.1',
    packages=[
        'geothermpy'
    ],
    url='https://github.com/MineralsCloud/geothermpy',
    license='MIT',
    author='Qi Zhang',
    author_email='qz2280@columbia.edu',
    description='A package that can calculate geotherm',
    install_requires=[
        'numba',
        'numpy',
        'pandas',
        'scipy',
        'matplotlib',
    ],
)
