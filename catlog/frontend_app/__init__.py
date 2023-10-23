"""
__init__.py
author: Zicheng Zeng
date: 2023/9/26
description: 网站前端（用户和后台管理）
"""
from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # 注册蓝图
    if config.BLUEPRINT:
        from catlog.frontend_app.main import main as main_blueprint
        app.register_blueprint(main_blueprint)

    # 初始化数据库
    if config.DATABASE:
        from catlog.db import db
        db.init_app(app)
        with app.app_context():
            db.create_all()

    return app
