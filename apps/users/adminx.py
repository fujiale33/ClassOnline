# -*- coding: utf8 -*-
__author__ = 'Colorful'
__date__ = '2018/1/23 下午5:01'
import xadmin
from xadmin import views
from .models import EmailVerifyRecord
from .models import Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch=True


class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = 'accordion'


# 注册邮箱到后台管理系统
class EmailVerifyRecordAdmin(object):
    list_display = ['id','code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['id','code', 'email', 'send_type', 'send_time']


# 注册轮播图到后台管理系统
class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'inage','url', 'index']
    list_filter =['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
