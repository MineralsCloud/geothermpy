# -*- coding: utf-8 -*-
"""
    Setup file for geothermpy.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.2.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import codecs
import os
import re
import sys
from distutils.core import setup

import setuptools
from pkg_resources import VersionConflict, require

try:
    require('setuptools>=38.3')
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)

# Referenced from `here <https://packaging.python.org/guides/single-sourcing-package-version/>`_.
here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(name='geothermpy',
    #   version=find_version('src', 'geothermpy', '__init__.py'),
      description='A powerful tool for quasi-harmonic approximation',
      author='Reno',
      author_email='singularitti@outlook.com',
      maintainer='Reno',
      maintainer_email='singularitti@outlook.com',
      license='GNU General Public License 3',
      url='https://github.com/MineralsCloud/geothermpy',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Physics',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ],
      python_requires='>=3.6',
      keywords='thermodynamic-properties quasi-harmonic-approximation scientific-computation',
      install_requires=[
          'numpy',
          'pandas',
          'scipy',
      ],
      packages=[
          'geothermpy',
      ])
