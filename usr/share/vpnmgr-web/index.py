#!/usr/bin/env python3
# -*-coding: utf-8 -*-

from lib.Html import Html

html = Html()
title = html.getPageTitle()
content_type = html.getContentType()
pages = ["start", "CAs", "Criar_usuario", "Criar CAs", "Listar_CAs", "Listar_certificados"]
title = "Página de login"

print(content_type)

print("<DOCTYPE html>")
print("<html>")
print(" <head>")
print("     <meta charset='utf-8'>")
print("     <title>")
print("     " + title)
print("     </title>")
print(" </head>")
print("<body>")
print(" <header>")
print("     <h1>" + title + "</h1>")
print(" </header>")
print("<main>")
print(" <section>")
print("     <form action='login.py' method='GET'>")
print("         <label for='login'>Login</label>")
print("         <input type='text' name='login' placeholder='Nome do usuário' required'>")
print("         <label for='password'>Password:</label>")
print("         <input type='password' name='password' placeholder='Password' required'>")
print("         <input type='submit' value='Acessar''>")
print("     </form>")
print(" </section>")
print("</main>")
print("<footer>")
print("<p>Todos os direitos reservados")
print("</footer>")
print("</body>")
print("</html>")