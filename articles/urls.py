from django.conf.urls import url
from . import views
import default

urlpatterns = [
    url(r'^a/(?P<id>[0-9]+)/$', views.show_article),
    url(r'^comment/action',default.views.post_comment,name='comment_action'),
    ]