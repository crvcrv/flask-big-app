#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.peewee.db import Database
db = Database()

from flask.ext.mail import Mail
mail = Mail()

from flask.ext.cache import Cache
cache = Cache()

from flask.ext.login import LoginManager
login_manager = LoginManager()

from flask.ext.openid import OpenID
oid = OpenID()