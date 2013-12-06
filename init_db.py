#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import random
import peewee
import settings

from app import db

database = db

def rstr(length=5):
    """
    random string
    """
    chars_lower = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    chars = chars_lower + chars_lower.upper()
    chars = chars.split()
    val = list()
    for i in range(length):
        val.append(chars[random.randint(0, len(chars)-1)])
    return ''.join(val)


if __name__ == '__main__':
    import pdb