from flask import redirect, request, flash, render_template, url_for

from . import user_blueprint
from .forms import RegisterForm, LoginForm


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST":
        # 验证表单
        if form.validate_on_submit():
            # 如果代码能走到这个地方，那么就代码表单中所有的数据都能验证成功
            username = form.username
            password = form.password
            password2 = form.password2
            # 假装做注册操作
            print(username, password, password2)
            return redirect(url_for('user_bp.login'))
        else:
            flash("参数有误或者不完整")

    return render_template('register.html', form=form)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        # 验证表单
        if form.validate_on_submit():
            # 如果代码能走到这个地方，那么就代码表单中所有的数据都能验证成功
            username = form.username
            password = form.password
            # 假装做注册操作
            print(username, password)
            return "success"
        else:
            flash("参数有误或者不完整")

    return render_template('login.html', form=form)

