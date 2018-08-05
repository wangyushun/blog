from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired, EqualTo, Length

class RegisterForm(FlaskForm):
    username = StringField(
        label="用户名：",
        validators=[DataRequired("请输入用户名"), Length(min=6, max=16, message='请输入6-16位字母或数字')],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入用户名",
        }
    )
    password = PasswordField(
        label="密码：",
        validators=[DataRequired("请输入密码"), Length(min=6, max=16, message='请输入6-16位字母或数字')],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码",
        }
    )
    password2 = PasswordField(
        label="确认密码：",
        validators=[
            DataRequired("请输入确认密码"),
            Length(min=6, max=16, message='请输入6-16位字母或数字'),
            EqualTo("password", "两次输入密码不一致")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入确认密码",
        }
    )
    submit = SubmitField(
        label="注册",
        render_kw={
            "class": "btn btn-info",
        }
    )


class LoginForm(FlaskForm):
    username = StringField(
        label="用户名：",
        validators=[DataRequired("请输入用户名")],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入用户名或邮箱",
        }
    )
    password = PasswordField(
        label="密码：",
        validators=[DataRequired("请输入密码")],
        render_kw={
            "placeholder": "请输入用户名",
            'class': 'form-control'
        }
    )
    submit = SubmitField(
        label="登陆",
        render_kw={
            'class': 'btn btn-info'
        }
    )


class NicknameForm(FlaskForm):
    nickname = StringField(
        label="新昵称：",
        validators=[DataRequired("请输入新昵称")],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新昵称",
        }
    )
    submit = SubmitField(
        label="提交",
        render_kw={
            'class': 'btn btn-info'
        }
    )


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(
        label="旧密码：",
        validators=[DataRequired("请输入旧密码"), Length(min=6, max=16, message='请输入6-16位字母或数字')],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入旧密码",
        }
    )
    new_password = PasswordField(
        label="密码：",
        validators=[DataRequired("请输入密码"), Length(min=6, max=16, message='请输入6-16位字母或数字')],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码",
        }
    )
    new_password2 = PasswordField(
        label="确认密码：",
        validators=[
            DataRequired("请输入确认密码"),
            Length(min=6, max=16, message='请输入6-16位字母或数字'),
            EqualTo("new_password", "两次输入密码不一致")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入确认密码",
        }
    )
    submit = SubmitField(
        label="修改",
        render_kw={
            "class": "btn btn-info",
        }
    )
