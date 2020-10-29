#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi

print("Content-type: text/html\n\n")

form = cgi.FieldStorage()

usuario = form.getvalue('name')
senha = form.getvalue('password')
print("<p>")
print("Nome de usuário: {0}<br>".format(usuario))
print("Senha : {0} <br>".format(senha))
print("</p>")
