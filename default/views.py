from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from . import models
from django import forms
from django.contrib.sessions.backends.db import SessionStore

class UserForms(forms.Form):
    username = forms.CharField()

def index(request):
    x = models.articles.objects.all()[:10]
    y = models.comments.objects.all()
    return render(request,'index.html',{'articles':x,'comments':y,'i':0})

def comments(request):
    x = models.comments.objects.all()
    return render(request,'article.html',{'comments':x})

def date_articles(request,date):
    x = models.articles.objects.filter(date=date)
    return render(request,'dateArticles.html',{'articles':x})

def register(request):
    sex = ((True,'男'),(False,'女'))
    return render(request, 'register.html',{'sex':sex})

def register_action(request):
    username = request.POST.get('username','USRENAME')
    #判断是否用户名重复
    try:
        if models.users.objects.get(username=username):
            return HttpResponseRedirect('/index/register')
    except:
        passwd = request.POST.get('passwd','PASSWD')
        #passwd = password(passwd)          #后续密码加密改进
        sex = request.POST.get('sex','SEX')
        birthday = request.POST.get('birthday','BIRTHDAY')
        tel = request.POST.get('tel','TEL')
        person_site = request.POST.get('person_site','PERSON_SITE')
        about_me = request.POST.get('about_me','ABOUT_ME')
        #保存用户注册信息
        models.users.objects.create(username=username,passwd=passwd,sex=sex,birthday=birthday,tel=tel,person_site=person_site,about_me=about_me)
        return HttpResponseRedirect('/index/login')


def login_action(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username','USERNAME')
            user = models.users.objects.get(username=username)
        except:
            html = '<script>alert("账号不存在！ 请重新输入");window.location.href="../";</script>'
            return HttpResponse(html)
        #uf = UserForms(request.POST)
        if request.POST.get('passwd', 'PASSWD') == user.passwd:
            request.session['user_id'] = user.id
            return render(request,'account.html',{'user':user,'log':'登录成功！'})
        else:
            html = '<script>alert("密码错误！ 请重新输入");window.location.href="../";</script>'
            return HttpResponse(html)
    else:
        html = '<script>alert("非法请求！ 已记录非法请求IP");window.location.href="../";</script>'
        return HttpResponse(html)

def logout(request):
    try:
        del request.session['user_id']
    except:
        html = '<script>alert("你还没有登录！");window.location.href="../";</script>'
        return HttpResponse(html)
    return HttpResponseRedirect('/index')


def account(request,username):
    user = models.users.objects.get(username=username)
    #user.sex是boolenfild数据类型
    sex_switch = {True:'男',False:'女'}
    user.sex = sex_switch[user.sex]
    articles = models.articles.objects.all()
    return render(request,'account.html',{'user':user,'sex':user.sex,'articles':articles})

def user_articles(request,username):
    articles = models.articles.objects.get(username=username)
    return render(request,'user_articles.html',{'articles':articles})

def new_article(request):
    title = request.POST.get('title','TITLE')
    try:
        models.articles.objects.get(title=title)
        html = '<script>alert("与已有文章重名了 ！");window.location.href="../";</script>'
        return HttpResponse(html)
    except:
        context = request.POST.get('context','CONTEXT')
        #应先取出已登录用户。。
        user = models.users.objects.all()[0]
        models.articles.objects.create(title=title,context=context,auth=user)
    return HttpResponseRedirect('/index/')

def post_comment(request):
    AR = models.articles.objects.get(title=request.POST.get('comment_for','COMMENT_FOR'))
    context = request.POST.get('context','CONTEXT')
    user = models.users.objects.all()[0]
    models.comments.objects.create(comment_for=AR,context=context,username=user)
    AR.comments_count += 1
    AR.save()
    html = '<script>alert("评论成功 ");window.location.href="../";</script>'
    return HttpResponse(html)

def edit_profile(request,username):
    user = models.users.objects.get(username=username)
    return render(request,'edit_profile.html',{'user':user})

def edit_profile_action(request):
    user = models.users.objects.get(username=request.POST.get('username'))
    user.passwd = request.POST.get('passwd')
    user.signature = request.POST.get('signature')
    user.birthday = request.POST.get('birthday')
    user.sex = request.POST.get('sex')
    user.tel = request.POST.get('tel')
    user.person_site = request.POST.get('person_site')
    user.about_me = request.POST.get('about_me')
    user.save()
    return 0