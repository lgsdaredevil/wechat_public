# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-04-28
    
"""
import hashlib

import time
from flask import render_template, request

from app import app


class CopyWords:
    def __init__(self):
        self.template_folder = 'templates'

    @staticmethod
    @app.route('/')
    def test():
        return '<h1>Hello world</h1>'

    @staticmethod
    @app.route('/test1')
    def test1():
        return render_template('test/test.html')


