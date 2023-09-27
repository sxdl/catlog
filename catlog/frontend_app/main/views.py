"""
views.py
author: Zicheng Zeng
date: 2023/9/26
description: 
"""
from flask import render_template, redirect, url_for, abort, flash, request, current_app, make_response
from . import main
from catlog.db import db, User, Role


@main.route('/', methods=['GET', 'POST'])
def index():
    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_john = User(username='john', role=admin_role)
    user_susan = User(username='susan', role=user_role)
    user_david = User(username='david', role=user_role)
    db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])
    db.session.commit()
    print(admin_role.id)
    print(mod_role.id)
    print(user_role.id)
    return render_template('index.html')

