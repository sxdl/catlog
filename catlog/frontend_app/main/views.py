"""
views.py
author: Zicheng Zeng
date: 2023/9/26
description: 
"""
from flask import render_template, redirect, url_for, abort, flash, request, current_app, make_response
from . import main
from catlog.db import db, User, Role

from flask_login import login_required, current_user
from flask import session


'''
前台路由
'''

@main.route('/')
@main.route('/index')
def index():
    return render_template('user/index.html')


@main.route('/trends', methods=['GET', 'POST'])
def trends():
    return render_template('user/trends_page.html')


@main.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('user/about_page.html')


@main.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user/user_page.html')

# TODO: 不太清楚如何对发布动态进行前后端分离，先在这里写一个实现功能，后面请教之后再改
@main.route('/post', methods=['GET', 'POST'])
# @login_required
def post():
    if request.method == 'GET':
        return render_template('user/post_page.html')
    else:
        pass

        


'''后台路由'''
@main.route('/manage/', methods=['GET', 'POST'])
@main.route('/manage', methods=['GET', 'POST'])
def manage_index():
    return render_template('manage/index.html')


@main.route('/manage/cats', methods=['GET', 'POST'])
def manage_cats():
    return render_template('manage/cats_manage.html')


@main.route('/manage/trends', methods=['GET', 'POST'])
def manage_trends():
    return render_template('manage/trends_manage.html')


@main.route('/manage/activities', methods=['GET', 'POST'])
def manage_activities():
    return render_template('manage/activities_manage.html')


@main.route('/manage/tasks', methods=['GET', 'POST'])
def manage_tasks():
    return render_template('manage/tasks_manage.html')


@main.route('/manage/logs', methods=['GET', 'POST'])
def manage_logs():
    return render_template('manage/logs_manage.html')


@main.route('/manage/feedbacks', methods=['GET', 'POST'])
def manage_feedbacks():
    return render_template('manage/feedbacks_manage.html')
