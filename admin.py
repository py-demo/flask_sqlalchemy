# coding=utf-8
from flask import Flask, render_template, jsonify
from flask_admin import Admin, BaseView, expose
from flask_login import LoginManager

from models.model import db, User
from config import config

app = Flask(__name__)
app.config.from_object(config)

admin = Admin(app, name='后台管理', template_mode='bootstrap3')
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


class Main(BaseView):
    @expose('/')
    def main(self):
        return self.render('admin/main.html')


admin.add_view(Main(name='方案', endpoint='main', category='系统管理'))
admin.add_view(Main(name='登录', endpoint='login', category='用户管理'))


@app.route('/', methods=['GET', 'POST'])
def index():
    users = User.query.all()
    arr = []
    for user in users:
        arr.append({
            'cname': user.cname,
            'ename': user.ename,
            'password': user.password,
            'is_admin': user.is_admin,
            'company_id': user.company_id,
            'enabled': user.enabled
        })

    return render_template('admin/login.html')


if __name__ == '__main__':
    app.run()
