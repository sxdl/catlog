"""
main.py
author: Zicheng Zeng
date: 2023/9/26
description: 应用入口
"""
import catlog
from werkzeug.serving import run_simple

app = catlog.create_app('debug')
# app.run()
run_simple('localhost', 5000, app)
