"""
__init__.py
author: Zicheng Zeng
date: 2023/9/26
description: 
"""
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import catlog.frontend_app as frontend
import catlog.backend_app as backend
from catlog.config import config


def create_app(config_name):
    cnfg = config[config_name]
    frontend_application = frontend.create_app(cnfg)
    backend_application = backend.create_app(cnfg)
    if cnfg.BLUEPRINT:
        application = DispatcherMiddleware(frontend_application, {
            '/api': backend_application
        })
        return application
    else:
        return frontend_application, backend_application
