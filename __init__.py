__author__ = 'Filip Wachowiak'
"""Backend strony internetowej cały czas w budowie"""
from os import path
import gc
from functools import wraps
from flask import Flask, render_template, flash, request, redirect, url_for, session, send_file
from content_management import Content, python_content, gpu_content, likes_setter, likes_getter, kotlin_content
from pymysql import escape_string as thwart
from passlib.hash import sha256_crypt
from wtforms import Form, validators, StringField, PasswordField, BooleanField
from dbconnect import connection
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='biuro.tkgf@gmail.com',
    MAIL_PASSWORD=''
)
mail = Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///likes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.app = app
db.init_app(app)

app.static_path = path.join(path.abspath(__file__), 'static')


app.secret_key = "klawy sekret"

if __name__ == "__main__":
    from views import *
    app.run(debug=True, host='77.55.221.165', port=5003)
