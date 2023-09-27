"""
views.py
author: Zicheng Zeng
date: 2023/9/26
description: 
"""
from flask import render_template, redirect, url_for, abort, flash, request
from . import main
from catlog.db import db, User, Role


@main.route('/', methods=['GET', 'POST'])
def index():
    admin_rol = Role(name='Admi')
    mod_rol = Role(name='Moderato')
    user_rol = Role(name='Use')
    user_joh = User(username='joh', role=admin_rol)
    user_susa = User(username='susa', role=user_rol)
    user_davi = User(username='davi', role=user_rol)
    db.session.add_all([admin_rol, mod_rol, user_rol, user_joh, user_susa, user_davi])
    db.session.commit()
    print(admin_rol.id)
    print(mod_rol.id)
    print(user_rol.id)
    return render_template('index.html')
