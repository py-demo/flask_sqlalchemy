#### 查看项目依赖
```base
pip list --format=columns
```

<pre>
Package          Version
---------------- -------
click            6.7
Flask            0.12.2
Flask-Admin      1.4.2
Flask-Login      0.4.1
Flask-SQLAlchemy 2.0
Flask-WTF        0.14.2
gunicorn         19.7.1
itsdangerous     0.24
Jinja2           2.10
MarkupSafe       1.0
pip              9.0.1
setuptools       28.8.0
SQLAlchemy       1.1.15
Werkzeug         0.13
WTForms          2.1
</pre>

- Windows系统没这个还真没法玩
> MySQL_python-1.2.5-cp27-none-win_amd64.whl

> https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python


#### 安装虚拟环境
```base
virtualenv venv
```


- 安装或升级：

> pip freeze > requirements.txt


- 导入\安装：
> pip install -r requirements.txt