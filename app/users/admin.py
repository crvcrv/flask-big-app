#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_peewee.admin import ModelAdmin

from wtforms import fields
from wtforms import Form
from wtfpeewee.orm import model_form, model_fields

from app.users.models import User, ResetPassword, UserFriend, Settings

class UserAdmin(ModelAdmin):
    model = User
    columns = ('id', 'username', 'email','active', 'activated', 'admin')
    filter_fields = ('username',)
    #exclude = ('salt',)

    def get_form(self, adding=False):
        # dirty form generator to include the hashed password value
        allow_pk = adding and not self.model._meta.auto_increment

        field_dict = model_fields(self.model,
            allow_pk = allow_pk, 
            only = self.fields, 
            exclude = self.exclude,
            converter = self.form_converter(self)
        )

        field_dict['password'] = fields.StringField(default=self.model._password)

        return type(self.model.__name__ + 'Form', (Form, ), field_dict)


class ResetPasswordAdmin(ModelAdmin):
    model = ResetPassword
    columns = ('user__username', 'created', 'expiry',)
    #exclude = ('created_date',)

class UserFriendAdmin(ModelAdmin):
    model = UserFriend
    columns = ('user', 'friend', 'blocked', 'accepted')

class SettingsAdmin(ModelAdmin):
    model = Settings
    columns = ('user', 'notification')