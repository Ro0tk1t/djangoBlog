from django.db import models
#from . import *

class articles(models.Model):
    title = models.CharField(max_length=32,default='test')
    auth = models.ForeignKey('users',on_delete=models.CASCADE,name='auth')
    date = models.DateTimeField('Posted in ',auto_now=True)
    type = models.CharField(max_length=20,default='随笔')
    comments_count = models.IntegerField(default=0)
    context = models.TextField(null=True)

    def __str__(self):
        return self.title

class comments(models.Model):
    comment_for = models.ForeignKey('articles',on_delete=models.CASCADE)
    username = models.ForeignKey('users',on_delete=models.CASCADE,name='username')
    date = models.DateTimeField('Posted in ',auto_now=True)
    context = models.TextField()

    def __str__(self):
        return self.context

class users(models.Model):
    username = models.CharField(max_length=30)
    passwd = models.CharField(max_length=30)
    sex = models.BooleanField(choices=((True,'男'),(False,'女')))
    birthday = models.DateTimeField('生日 ',null=True)
    register_date = models.DateTimeField('注册日期',auto_now=True)
    tel = models.CharField('手机号',max_length=11,null=True)
    article_count = models.IntegerField('文章数',default=0)
    person_site = models.CharField('个人站点',max_length=20,null=True)
    signature = models.TextField(max_length=60,null=True)
    about_me = models.TextField(null=True)

    def __str__(self):
        return self.username

class lable(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class link(models.Model):
    type = models.CharField(max_length=20,choices=(('friend_blog','友情博客'),('friend_link','友情链接'),('knowledge_library','知识库')))
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.name