#!/usr/bin/env python

from setuptools import setup

setup(
    name='lektor-brunch-support',
    version='0.1',
    description='Adds support for Brunch to Lektor.',
    url='http://github.com/lektor/lektor-brunch-support',
    author='Severen Redwood',
    author_email='severen@shrike.me',
    license='MPL-2.0',
    py_modules=['lektor_brunch_support'],
    entry_points={
        'lektor.plugins': [
            'brunch-support = lektor_brunch_support:BrunchSupportPlugin',
        ],
    },
)
