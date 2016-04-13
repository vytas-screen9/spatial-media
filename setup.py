# -*- coding: utf-8 -*-
"""
Spatial Media

A collection of specifications and tools for 360° video and spatial audio,
including:
 * Spatial audio metadata specification
 * Spherical video metadata specification
 * Spatial media tools for injecting spatial media metadata in video files
"""

# Always prefer setuptools over distutils
from setuptools import find_packages
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='spatialmedia',
    version='0.0.1',
    description=('A collection of specifications and tools '
                 'for 360° video and spatial audio'),
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/google/spatial-media',

    # Maintainer details
    maintainer='Vytautas Liuolia',
    maintainer_email='vytautas.liuolia@screen9.com',

    # Licence
    license='Apache License 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Video',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='spatial audio spherical stitched equirectangular video',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),
)
