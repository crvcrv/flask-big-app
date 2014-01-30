#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import hmac
import random

def rstr(length=5, special_chars=True, numbers=True, upper_case=True):
    chars_lower = 'a b c d e f g h i j k l m n o p q r s t u v w x y z '
    n = '1 2 3 4 5 6 7 8 9 0 '
    special = '! $ % & / ( ) * + - _ < > = ? # '

    chars = chars_lower
    if upper_case:
        chars += chars_lower.upper()
    if numbers:
        chars += n
    if special_chars:
        chars += special

    chars = chars.split()
    val = list()
    for i in range(length):
        val.append(chars[random.randint(0, len(chars)-1)])
    return ''.join(val)

def salt(length=10, digestmod=hashlib.md5):
    rnd = rstr(length=length)
    h = hmac.new(rnd, digestmod=digestmod)
    return h.hexdigest()