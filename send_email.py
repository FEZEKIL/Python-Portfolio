import smtplib, ssl
from http import server

host = "smtp.gmail.com"
port = 465

username = "gxalaba.fezekile@gmail.com"
password = "roynsrcsynkzrpfw"

reciever = "gxalaba.fezekile@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
Bye!
"""
with smtplib.SMTP_SSL(host, port,context= context) as server:
    server.login(username, password)
    server.sendmail(username, reciever, message )
