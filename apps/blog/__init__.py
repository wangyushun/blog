from flask import Blueprint

blog_blueprint = Blueprint('blog_bp', __name__, template_folder='templates')

# 使用了蓝图的view必须在蓝图实例后倒入
from . import view
