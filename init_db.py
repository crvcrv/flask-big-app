#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import random
import peewee
import settings

from app import *
from app.feed.models import *
from app.message.models import *
from app.posts.models import *
from app.users.models import *

from app.utils import rstr
database = db #peewee.SqliteDatabase('dev.db')
#database = peewee.MySQLDatabase('px', host='127.0.0.1', port=3306, user='px', passwd='px')

def random_gps(min_latitude=50, max_latitude=52, min_longitude=6, max_longitude=8):
    diff_lati = max_latitude - min_latitude - 1
    diff_longi = max_longitude - min_longitude - 1

    rand_lati = min_latitude + random.randint(0, diff_lati) + random.random()
    rand_long = min_longitude + random.randint(0, diff_longi) + random.random()

    return {
        'latitude': '{:f}'.format(rand_lati),
        'longitude': '{:f}'.format(rand_long),
    }



if __name__ == '__main__':
    import pdb
    #pdb.set_trace()
    #database.connect()
    try:
        User.create_table()
        ResetPassword.create_table()
        Message.create_table()
        Settings.create_table()
        UserFriend.create_table()
        Comment.create_table()
        Post.create_table()
        GPS.create_table()
    except:
        pass

    # create data
    times = 10
    for i in range(times):
        u1 = User(
            username = rstr(10),
            email = rstr()+'@'+rstr()+'.com',
            first_name = rstr(10),
            last_name = rstr(20),
            avatar = rstr(),
            gender = 'm',
            created = datetime.datetime.now(),
            last_login = datetime.datetime.now(),
            activated = True
        )
        u1.set_password(rstr())
        u1.save()

    #create settings
    for j in range(times):
        u2 = Settings(
            user = j+1,
            notification = True
        )
        u2.save()

    #create admin
    u = User(
            username = 'admin',
            email = 'admin@admin.de',
            first_name = 'admin',
            last_name = 'admin',
            avatar = rstr(),
            gender = 'm',
            created = datetime.datetime.now(),
            last_login = datetime.datetime.now(),
            activated = True,
            admin = True
        )
    u.set_password('admin')
    u.save()

    # create gps

    for i in range(times):
        rand_gps = random_gps()

        g = GPS.create(
            latitude = rand_gps.get('latitude'),
            longitude = rand_gps.get('longitude'),
            accuracy = 1,
            created = datetime.datetime.now()
        )
