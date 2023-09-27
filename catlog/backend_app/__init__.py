"""
__init__.py
author: Zicheng Zeng
date: 2023/9/26
description: 后台应用
"""
from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    # 注册蓝图
    from catlog.backend_app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 初始化数据库
    from catlog.db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
