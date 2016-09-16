#!/usr/bin/env python

from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except TypeError:
    # Python 2.x compat.
    import codecs
    with codecs.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='lektor-brunch-support',
    version='0.1.0',
    description='Adds support for Brunch to Lektor.',
    long_description=long_description,
    url='http://github.com/lektor/lektor-brunch-support',
    author='Severen Redwood',
    author_email='severen@shrike.me',
    license='MPL-2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='lektor plugin',
    py_modules=['lektor_brunch_support'],
    entry_points={
        'lektor.plugins': [
            'brunch-support = lektor_brunch_support:BrunchSupportPlugin',
        ],
    },
)
