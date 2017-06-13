# -*- coding: utf-8 -*-
"""
behave-cmdline
"""
from setuptools import setup, find_packages
import os

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.rst')).read()

VERSION = '1.3.0'

setup(name='environconfig',
      version=VERSION,
      description=("Application configuration from environment "
                   "variables made easy"),
      long_description=README,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='environment variables configuration',
      author='Roberto Abdelkader Martínez Pérez',
      author_email='robertomartinezp@gmail.com',
      url='https://github.com/buguroo/environconfig',
      license='LGPLv3',
      py_modules=["environconfig"],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ])
