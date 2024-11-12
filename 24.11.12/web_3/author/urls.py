__author__ = 'wilkinsddvd'
__version__ = '1.0'

# 引入依赖的模块
from django.urls import path,include
from . import views

# 路由模块名称
app_name = 'author'

# 添加路由配置
urlpatterns = [
    path('register/', views.author_register, name='register'),\
    path('login/', views.author_login, name='login'),
]