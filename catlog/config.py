"""
config.py
author: Zicheng Zeng
date: 2023/9/26
description: flask配置文件
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DATABASE = False
    BLUEPRINT = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭对模型修改的监控

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DATABASE = True
    BLUEPRINT = True

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '../data-dev.db')


class TestingConfig(Config):
    TESTING = True


class EmptyConfig(Config):
    DATABASE = True
    BLUEPRINT = False

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, '../data-empty-dev.db')


class ProductionConfig(Config):
    pass


config = {
    'debug': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'empty': EmptyConfig, # 返回一个没有定义过views的包含一个数据库的新app

    'default': DevelopmentConfig
}