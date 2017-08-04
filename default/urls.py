from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'register/action/$',views.register_action,name='register_action'),
    url(r'^login/$',TemplateView.as_view(template_name='login.html')),
    url(r'^logout$',views.logout),
    url(r'^account/$', views.login_action,name='login_action'),
    url(r'^account/(?P<username>[0-9A-z]+)/$',views.account),
    url(r'^account/articles/$',views.user_articles,name='user_articles'),
    url(r'^new/article/$',TemplateView.as_view(template_name='new_article.html')),
    url(r'^new/article/action/$',views.new_article,name='new_article_action'),
    url(r'^edit/profile/(?P<username>[0-9A-z]+)/$',views.edit_profile,name='edit_profile'),
    url(r'^profile/$',views.edit_profile_action,name='edit_profile_action')
    #url(r'^articles/date/(?P<date>[.*?])/$',views.date_articles,name='date_articles'),
]
