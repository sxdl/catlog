# 开发日志

## 20230926 #structure_0.0.1

搭建前后台页面框架，测试：

`(venv) python main.py`

(ide直接debug main.py文件就行)

效果: 直接访问localhost:5000 显示"hello frontend",访问localhost:5000/backend 显示“hello backend”

## 20230927 #structure_0.0.2

配置sqlite数据库，测试：

`(venv) python main.py`

效果：根目录下生成data-dev.db文件；控制台输出数据库中的所有数据

TODO: 需要在db.py中补充数据库的增删改查操作以及数据表的定义

## 20230928 #structure_0.0.4

完成前后台页面导航简略实现，后续可以直接做面向对象设计

效果：前台和后台（/backend）的简单导航界面，可以实现页面跳转
