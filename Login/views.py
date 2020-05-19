from flask import Blueprint
from flask import redirect

blue = Blueprint('blue', __name__, template_folder='templates', static_folder='static')

from flask import render_template
from flask import request
from Login.models import User

@blue.route('/tologin/')
def tologin():
    error_massage = request.args.get('error','')
    return render_template('tologin.html',error_massage = error_massage)

@blue.route('/login/', methods = ['POST'])
def login():
    username = request.form.get('username','')
    password = request.form.get('password','')

    num = User.query.filter_by(username = username).count()
    if num != 0:
        user_list = User.query.filter_by(username = username).all()
        for user in user_list:
            if user.password == password:
                return 'password is right'
        error_password = '密码错误'
        return redirect('/tologin?error=%s'%error_password)
    else:
        error_user = '用户不存在，请注册'
        return redirect('/tologin?error=%s'%error_user)
















