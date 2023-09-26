"""
__init__.py.py
author: Zicheng Zeng
date: 2023/9/26
description: 
"""
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
