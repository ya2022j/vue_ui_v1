




from flask import Flask,render_template,redirect,request,session
# from flask_login import LoginManager




app = Flask(__name__)

app.secret_key = 'admin'  # 对用户信息加密


@app.route('/login', methods=['GET', "POST"])  # 路由默认接收请求方式位POST，然而登录所需要请求都有，所以要特别声明。
def login():
    if request.method == 'GET':
        return render_template('netbox_login_copy.html')
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'admin':  # 这里可以根据数据库里的用户和密码来判断，因为是最简单的登录界面，数据库学的不是很好，所有没用。
        session['user_info'] = username
        return redirect('/')
    else:
        return render_template('netbox_login_copy.html', msg='用户名或密码输入错误')

@app.route('/')
def index():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    return 'hello'






    # return render_template('netbox_login_copy.html')









if __name__ == "__main__":
    app.run()
