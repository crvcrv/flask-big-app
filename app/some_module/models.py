#!/usr/bin/env python
# -*- coding: utf-8 -*-
import peewee
from app import db

database = db

class BaseModel(peewee.Model):
    class Meta:
        database = database