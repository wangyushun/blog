from flask import redirect, request, flash, render_template, url_for

from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import or_

from apps import db
from . import user_blueprint, login_manager
from .forms import RegisterForm, LoginForm, NicknameForm, ChangePasswordForm
from .models import User


login_manager.login_view = 'user_bp.login'
login_manager.login_message = '需要登陆后才可继续访问'


@user_blueprint.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():
    form = RegisterForm(request.form)
    if request.method == "POST":
        # 验证表单
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            # 新建用户
            user = User(username=username, password=password)
            if User.is_username_exists(username=username):
                flash("用户名已存在")
            else:
                try:
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for('user_bp.login'))
                except Exception:
                    flash("注册失败")
        else:
            flash("输入有误，请按错误提示重新输入")

    return render_template('register.html', form=form)


@user_blueprint.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        # 验证表单
        if form.validate_on_submit():
            username_or_email = form.username.data
            password = form.password.data
            user = User.query.filter(or_(User.username==username_or_email, User.email==username_or_email)).first()
            if not user:
                flash('用户名不存在')
            elif user.check_password(password):
                login_user(user)
                next = request.args.get('next', url_for('blog_bp.blog'))
                return redirect(next)
            else:
                flash("密码错误")
        else:
            flash("输入有误，请按错误提示重新输入")

    return render_template('login.html', form=form)



@user_blueprint.route('/logout', endpoint='logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog_bp.blog'))


@user_blueprint.route('/userinfo', endpoint='userinfo')
@login_required
def userinfo():
    return render_template('userinfo.html', user=current_user)


@user_blueprint.route('/nickname', methods=['GET', 'POST'], endpoint='change_nickname')
@login_required
def change_nickname():
    form = NicknameForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = current_user
            try:
                user.nickname = form.nickname.data
                db.session.commit()
                return redirect(url_for('user_bp.userinfo'))
            except Exception:
                flash('修改失败')
        else:
            flash('输入有误')

    return render_template('form_with_submit.html', title='修改昵称', form=form)


@user_blueprint.route('/password', methods=['GET', 'POST'], endpoint='change_password')
@login_required
def change_password():
    form = ChangePasswordForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            #验证旧密码
            old_password = form.old_password.data
            if current_user.check_password(old_password):
                try:
                    new_password = form.new_password.data
                    current_user.password = new_password
                    db.session.commit()
                except Exception:
                    flash('修改密码失败')
                    
                logout_user()  # 注销用户重新登陆
                return redirect(url_for('user_bp.login'))
            else:
                flash('旧密码错误')
    return render_template('form_with_submit.html', title='修改密码', form=form)

