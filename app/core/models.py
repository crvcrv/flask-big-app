#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from flask.ext.peewee import db
import peewee

class Model(db.Model):
    created = peewee.DateTimeField(default=datetime.datetime.now)

CompositeKey = peewee.CompositeKey
CharField = peewee.CharField
TextField = peewee.TextField
DateTimeField = peewee.DateTimeField
IntegerField = peewee.IntegerField
BooleanField = peewee.BooleanField
FloatField = peewee.FloatField
DoubleField = peewee.DoubleField
BigIntegerField = peewee.BigIntegerField
DecimalField = peewee.DecimalField
ForeignKeyField = peewee.ForeignKeyField
DateField = peewee.DateField
TimeField = peewee.TimeField
BlobField = peewee.BlobField
