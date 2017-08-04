from django.shortcuts import render
from . import models
import default

def show_article(request,id):
    #x = request.POST.get(id)
    ar = default.models.articles.objects.get(pk=id)
    co = default.models.comments.objects.filter(comment_for=ar.id)
    cos = default.models.comments.objects.all()[:10]
    ars = default.models.articles.objects.all()[:10]

    x = {'article':ar,'comment':co,'comments':cos,'articles':ars}
    try:
        up = default.models.articles.objects.get(pk=int(id)-1)
        x['up'] = up
    except:
        pass
    try:
        next = default.models.articles.objects.get(pk=int(id)+1)
        x['next'] = next
    except:
        pass

    return render(request,'article.html',x)

    #def show_comment(request,id):
    #    return 0