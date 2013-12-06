#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, views, jsonify
from werkzeug import check_password_hash, generate_password_hash

from app import db

mod = Blueprint('some_app', __name__, url_prefix='/some_app')

class SomeView(views.MethodView):
    def get(self, id=None):
        pass

    def post(self):
        pass

    def put(self, id=None):
        pass

    def delete(self, id=None):
        pass

mod.add_url_rule('/', view_func=SomeView.as_view('some_view'))