#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
from lib.Login import Login

form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

login = Login()

login.setUsername(username)