#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_peewee.db import Database

import settings

app = Flask(__name__)
app.config.from_object(settings.DevConfig)

db = Database(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.app.views import mod as mod_mod
app.register_blueprint(mod_mod)

# https://github.com/mitsuhiko/flask/wiki/Large-app-how-to
# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)