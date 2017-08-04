#from __future__ import absolute_import
from django.contrib import admin
from default.models import *

class article_admin(admin.ModelAdmin):
    list_display = ('title','auth','date','context')

class comment_admin(admin.ModelAdmin):
    list_display = ('username','comment_for','date','context')

class user_admin(admin.ModelAdmin):
    list_display = ('username','passwd','sex','tel','register_date','birthday','article_count','person_site')
admin.site.register(articles,article_admin)
admin.site.register(comments,comment_admin)
admin.site.register(users,user_admin)