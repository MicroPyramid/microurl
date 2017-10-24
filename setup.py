#!/usr/bin/env python
from setuptools import setup

setup(
    name='microurl',
    version='0.1.1',
    description='microurl is a python module to create minfied urls',
    author='MicroPyramid',
    author_email='hello@micropyramid.com',
    maintainer='Ashwin',
    maintainer_email='hello@micropyramid.com',
    url='http://github.com/micropyramid/microurl',
    license='GPL3',
    long_description=open('README.rst').read(),
    keywords='Url minifier python library using google, bitly',
    packages=['microurl'],
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    test_suite='tests.test_suite',
    zip_safe=True,
)
