from flask import Blueprint, render_template, request, redirect, url_for

blue = Blueprint('blue', __name__, template_folder='templates',
                 static_folder='static')

@blue.route('/tologin')
def tologin():
    return render_template('tologin.html')

@blue.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
    else:
        print('获取方法错误')
    return '已登陆'

@blue.route('/regist',methods=['GET','POST'])
def regist():
    return redirect(url_for('blue.tologin'))

