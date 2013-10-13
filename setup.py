#!/usr/bin/env python

from setuptools import setup

setup(
      name='microurl',
      version='0.0.1',
      #install_requires=['lxml', 'PIL'],
      description='microurl is a python module to create minfied urls',
      author='MicroPyramid',
      author_email='MicroPyramid@googlegroups.com',
      maintainer='Archana, Ashwin',
      maintainer_email='MicroPyramid@googlegroups.com',
      url='http://github.com/micropyramid/microurl',
      py_modules=['microurl'],
      
      license=open('LICENSE').read(),
      long_description=open('README.rst').read(),
      
      keywords = 'Url minifier python library using google, bitly, supr, dottk',
      packages=['microurl'],
      include_package_data=True,
      zip_safe=True,
      )
      
      
      
      
