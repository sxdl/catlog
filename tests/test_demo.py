"""
test_demo.py
author: Zicheng Zeng
date: 2023/10/23
description: 测试入口demo，使用'empty'配置一个只有数据库没有蓝图的flask app.在这里定义路由
"""
import catlog
from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware

frontend_app, backend_app = catlog.create_app('empty')


# ### 在这里定义frontend和backend的路由 ###
@frontend_app.route('/')
def front_index():
    return "hello eee"


@backend_app.route('/')
def back_index():
    return "hello backend"

# ########################################


app = DispatcherMiddleware(frontend_app, {'/api': backend_app})
run_simple('localhost', 5000, app)
