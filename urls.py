#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import views as app_views

urls = (
    ('/app/<id>', app_views.SomeView.as_view('some_view')),

)

