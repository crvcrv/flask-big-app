#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager

from app import create_app
from fbone.extensions import db
from fbone.user import User, UserDetail, ADMIN, ACTIVE
from fbone.utils import MALE


app = create_app()
manager = Manager(app)

@manager.command
def run():
    """Run in local machine."""

    app.run()


@manager.command
def initdb():
    """Init/reset database."""

    db.drop_all()
    db.create_all()

    #create admin
    u = User(
            username = 'admin',
            email = 'admin@admin.de',
            first_name = 'admin',
            last_name = 'admin',
            avatar = '',
            gender = 'm',
            created = datetime.datetime.now(),
            last_login = datetime.datetime.now(),
            activated = True,
            admin = True
        )
    u.set_password('admin')
    u.save()


manager.add_option('-c', '--config',
                   dest="config",
                   required=False,
                   help="config file")

if __name__ == "__main__":
    manager.run()
