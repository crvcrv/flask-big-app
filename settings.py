#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'Secret'

class DevConfig(Config):
    DEBUG = True
    DATABASE = {
        'name': 'dev.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }

class LiveConfig(Config):
    DEBUG = False