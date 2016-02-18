#!/usr/bin/env python

import sys

try:
    from setuptools import setup
except ImportError:
    print('Pyramid-Webpack needs setuptools in order to build. ' +
          'Install it using your package manager ' +
          '(usually python-setuptools) or via pip (pip install setuptools).')
    sys.exit(1)

setup(name='Pyramid-Webpack',
      version=open('VERSION', 'r').read()[:-1],
      author='Robert Duffner',
      author_email='rjduffner@gmail.com',
      url='https://github.com/rjduffner/pyramid_webpack',
      description='Pyramid extension for managing assets with Webpack.',
      license='GPLv3',
      install_requires=[
            'setuptools',
            'pyramid'
      ],
      tests_require=['pytest'],
      packages=['pyramid_webpack'],
      package_data={'Pyramid-Webpack': ['VERSION']},
      zip_safe=False,
      data_files=[])
