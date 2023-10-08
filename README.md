
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sxdl/catlog/master/catlog/frontend_app/static/img/Light_Cap_CatLog_LOGO_800-800.png">
    <img width="40%" align="center" alt="CatLog Logo" src="https://raw.githubusercontent.com/sxdl/catlog/master/catlog/frontend_app/static/img/Cap_CatLog_LOGO_800-800.png">
  </picture>
</p>

<h1 align="center">
  CatLog——貓皇志
</h1>
<p align="center">
  一个专注于记录猫主子活动的铲屎官交流平台
</p>

<p align="center">
  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Platform-Windows-blue?color=#4ec820" alt="Platform Windows"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/License-未定-blue?color=#4ec820" alt="MIT"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/github/stars/sxdl/catlog.svg?style=social" alt="GitHub stars"/>
  </a>



</p>


## 这个项目想做什么？
我们希望打造一个***有别于传统爱猫人士交流平台的论坛社区***.

这里的一切***以猫为本***(ﾐචᆽචﾐ)

毕竟有什么比我们所爱的猫猫更适合做这个社区的主人呢(=ඒᆽඒ=)
。。。（待补充）

## 项目结构

catlog是项目的根目录，其下包含三个文件夹和三个.py文件。

##### 文件夹：

* idea文件夹，是py的配置文件。

* back_end后端的代码。
  * main文件夹：

init.py：创建蓝图

errors.py：

views.py：

template文件夹：用于存放后端的html源码

init.py文件：定义create_app函数来创建后端

* front_end前端的代码。
  * main文件夹：

 __init__.py：创建蓝图

errors.py：

views.py：

template文件夹：用于存放后端的html源码。

init.py文件：定义create_app函数来创建前端

##### .py文件：

* init.py：定义Create_app函数，用于定义初始化前后端，以及接受请求方式。

* config.py：用于flask框架的调试。
  * Config类：用于初始化配置

DevelopmentConfig类：用于开发环境的配置，及指定数据库地址。

TestingConfig 类：用于设置测试相关的配置选项

ProductionConfig类：生产环境的配置类

config 字典：方便查看配置信息

* db.py，用于创建数据库。
  * 使用SQLAlchemy 库来定义了数据库模型类base。

创建db对象进行连接数据库、执行查询以及管理数据库模型。

定义了两个数据库模型类User和Roles

## 技术方案

flask + layui
