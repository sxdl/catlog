"""
__init__.py
author: Zicheng Zeng
date: 2023/9/26
description: 
"""
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import catlog.frontend_app as frontend
import catlog.backend_app as backend
from catlog.config import config


def create_app(config_name):
    frontend_application = frontend.create_app(config[config_name])
    backend_application = backend.create_app(config[config_name])
    application = DispatcherMiddleware(frontend_application, {
        '/backend': backend_application
    })
    return application
