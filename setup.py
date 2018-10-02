#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as f:
      long_desc = f.read()


setup(name='twols',
      version='0.0.1',
      author='John Tyree',
      author_email='johntyree@gmail.com',
      license='GPL3+',
      url='http://github.com/johntyree/twols',
      description='Grab bag of utilities.',
      long_description=long_desc,
      keywords='utils',
      py_modules=['twols'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: '
          'GNU General Public License v3 or later (GPLv3+)',
          'Topic :: Utilities',
          ],
      )
