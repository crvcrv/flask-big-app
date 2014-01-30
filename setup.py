#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

project = "flask-big-app"

setup(
    name=project,
    version='0.1',
    url='https://github.com/47bytes/flask-big-app',
    description='Flask Big App',
    author='RT',
    author_email='47bytes@gmail.com',
    packages=["flask-big-app"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-Admin',
        'Flask-WTF',
        'Flask-Script',
        'Flask-Testing',
        'Flask-Login',
        'Flask-Mail',
        'Flask-Cache',
        'Flask-OpenID',
        'peewee',
        'flask-peewee',
        'wtf-peewee',
        'nose',
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries'
    ]
)
