#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import hashlib
import json

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, views, jsonify, Response
from werkzeug import check_password_hash, generate_password_hash
import peewee

from app import db
from app.users.models import User, Settings, UserFriend
#from app.users.decorators import requires_login

mod = Blueprint('users', __name__, url_prefix='/users')

class UserListAPI(views.MethodView):
    """
    User
    / : get all user, create new user
    """
    def get(self):
        # get all user

        user_list = list()
        for user in User.select():
            user_list.append(user.serialize)

        return Response(json.dumps(user_list, indent=4), mimetype='application/json')

    def post(self):
        resp = request.get_json()
        avatar = resp.get('avatar')
        email = resp.get('email')
        username = resp.get('username')
        first_name = resp.get('first_name') or ''
        last_name = resp.get('last_name') or ''
        password = resp.get('password')
        gender = resp.get('gender') or ''


        user = User.create(
            avatar=avatar, 
            email=email, 
            first_name=first_name, 
            gender=gender,  
            last_name=last_name, 
            password=password,
            username=username,
            created=datetime.datetime.now(),
            last_login=datetime.datetime.now(),
            activated=False,
        )
        
        return Response(json.dumps(user.serialize), mimetype='application/json')

    def put(self, id=None):
        return Response(status=405)

    def delete(self, id=None):
        return Response(status=405)

class UserDetailAPI(views.MethodView):
    """
    User
    /<id> : get user, update user, deactivate user
    """
    def get(self, id=None):
        if id:
            try:
                user = User.get(id=id)
            except User.DoesNotExist:
                return Response(status=404)
            else:
                return Response(json.dumps(user.serialize), mimetype='application/json')
        else:
            return Response(status=404)

    def put(self, id=None):
        resp = request.get_json()
        if id:
            try:
                user = User.get(id=id)
            except User.DoesNotExist:
                return Response(status=404)
            else:
                user.avatar = resp.get('avatar', user.avatar)
                user.email = resp.get('email', user.email)
                user.username = resp.get('username', user.username)
                user.first_name = resp.get('first_name', user.first_name)
                user.last_name = resp.get('last_name', user.last_name)
                user.password = resp.get('password', user.password)
                user.gender = resp.get('gender', user.gender)
                user.save()

                return Response(json.dumps(user.serialize), mimetype='application/json')

        else:
            return Response(status=404)


    def post(self):
        return Response(status=405)

    def delete(self, id=None):
        resp = request.get_json()
        if id:
            try:
                user = User.get(id=id)
            except User.DoesNotExist:
                return Response(status=404)
            else:
                user.activated = resp.get('activated', user.activated)
                user.save()

                return Response(json.dumps(user.serialize), mimetype='application/json')

        else:
            return Response(status=404)


class UserSettingsAPI(views.MethodView):
    """
    Settings
    /<id>/settings/: get user settings
    """
    def get(self, id=None):
        if id:
            try:
                userSettings = Settings.get(user=id)
            except Settings.DoesNotExist:
                return Response(status=404)
            else:
                return Response(json.dumps(userSettings.serialize), mimetype='application/json')
        else:
            return Response(status=404)

    def post(self, id=None):
        #settings erstellen hier oder oben wenn ein neuer user erstellt wird?
        pass

    def put(self, id=None):
        resp = request.get_json()
        if id:
            try:
                userSettings = Settings.get(user=id)
            except Settings.DoesNotExist:
                return Response(status=404)
            else:
                userSettings.notification = resp.get('notification', userSettings.notification)
                userSettings.save()
                return Response(json.dumps(userSettings.serialize), mimetype='application/json')

        else:
            return Response(status=404)


class UserFriendsAPI(views.MethodView):
    """
    UserFriend
    /<id>/friends/ : get user friends, add new friend, block or accept friend
    """
    def get(self, id=None):
        if id:
            try:
                userFriend = UserFriend.select().where(UserFriend.user==id)
            except UserFriend.DoesNotExist:
                return Response(status=404)
            else:
                user_friendList = list()
                for friend in userFriend:
                    user_friendList.append(friend.serialize)

                return Response(json.dumps(user_friendList, indent=4), mimetype='application/json')
        else:
            return Response(status=404)


    def post(self, id=None):
        if id:
            try:
                User.get(id=id)
                #hier prüfen ob der user den freund schon besitzt oder via app mit /<id>/friends/ ?
            except User.DoesNotExist:
                return Response(status=404)
            else:
                #add new user friend
                resp = request.get_json()
                friend = resp.get('friend')
                accepted = resp.get('accepted') or False
                blocked = resp.get('blocked') or False

                friend = UserFriend.create(
                    user=id,
                    friend=friend,
                    accepted=accepted,
                    blocked=blocked, 
                )
            return Response(json.dumps(friend.serialize), mimetype='application/json')
        else:
            return Response(status=404)




    def put(self, id=None):
        #block or accept friend
        if id:
            try:
                resp = request.get_json()
                fr = resp.get('friend')
                userFriend = UserFriend.get(user=id,friend=fr)
            except UserFriend.DoesNotExist:
                return Response(status=404)
            else:
                resp = request.get_json()
                accepted = resp.get('accepted') or ''
                blocked = resp.get('blocked') or ''

                userFriend.accepted = resp.get('accepted', userFriend.accepted)
                userFriend.blocked = resp.get('blocked', userFriend.blocked)
                userFriend.save()

            return Response(json.dumps(userFriend.serialize), mimetype='application/json')
        else:
            return Response(status=404)

    def delete(self, id=None):
        #sollen wir den datensatz jeweils wirklich entfernen ?
        return jsonify(httpcode=404)


# user_list: get all user, create user
mod.add_url_rule('/', view_func=UserListAPI.as_view('user_list'))

# users/user/<id>: get single, update user, deactivate user 
mod.add_url_rule('/<int:id>/', view_func=UserDetailAPI.as_view('user'))

# users/user/settings/<int:id>
mod.add_url_rule('/<int:id>/settings/', view_func=UserSettingsAPI.as_view('user_settings'))

# users/user/friends/<int:id>
mod.add_url_rule('/<int:id>/friends/', view_func=UserFriendsAPI.as_view('user_friends'))

"""
@mod.route('/me/')
@requires_login
def home():
    return render_template("users/profile.html", user=g.user)

@mod.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

@mod.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    # make sure data are valid, but doesn't validate password is right
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # we use werzeug to validate user's password
        if user and check_password_hash(user.password, form.password.data):
            # the session can't be modified as it's signed, 
            # it's a safe place to store the user id
            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('users.home'))
        flash('Wrong email or password', 'error-message')
    return render_template("users/login.html", form=form)

@mod.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        # create an user instance not yet stored in the database
        user = User(name=form.name.data, email=form.email.data, \
            password=generate_password_hash(form.password.data))
        # Insert the record in our database and commit it
        db.session.add(user)
        db.session.commit()

        # Log the user in, as he now has an id
        session['user_id'] = user.id

        # flash will display a message to the user
        flash('Thanks for registering')
        # redirect user to the 'home' method of the user module.
        return redirect(url_for('users.home'))
    return render_template("users/register.html", form=form)
"""