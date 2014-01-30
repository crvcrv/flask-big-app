#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import hmac

from app.core import models

from app.utils import salt

class User(models.Model):
    username = models.CharField()
    email = models.CharField()
    _salt = models.CharField()
    _password = models.CharField()
    last_login = models.DateTimeField()
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    def password():
        doc = "The password property."
        def fget(self):
            return self._password
        def fset(self, value):
            if value != self.password:
                # very hacky workaround so hashed password doesn't get rehashed in admin.
                # remove condition later so there wont be any collisions
                self.set_password(value)
        return locals()
    password = property(**password())

    def set_password(self, password):
        s = salt()
        pw = hmac.new('{0}{1}'.format(s, password), digestmod=hashlib.sha512)

        self._salt = s
        self._password = pw.hexdigest()

    def check_password(self, password):
        pw = hmac.new('{0}{1}'.format(self.salt, password), digestmod=hashlib.sha512).hexdigest()
        if pw == self.password:
            return True
        return False

    def gravatar_url(self, size=80):
        return 'http://www.gravatar.com/avatar/{hash}?d=identicon&s={size}'.format(
            hash = hashlib.md5(self.email.strip().lower().encode('utf-8')).hexdigest(), 
            size = size
        )

    def __repr__(self):
        return self.username