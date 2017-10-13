#!/usr/bin/env python

from setuptools import setup

setup(name='sumbader',
    version='0.1',
    description='Sum the Bader charge of selected atoms',
    author='Davide Olianas',
    author_email='ubuntupk@gmail.com',
    py_modules=['sumbader'],
    entry_points={
        'console_scripts': ['sumbader=sumbader:main']
    }

    )
