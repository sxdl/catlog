"""
views.py
author: Zicheng Zeng
date: 2023/9/26
description: 
"""
from flask import render_template, redirect, url_for, abort, flash, request, current_app, make_response
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

