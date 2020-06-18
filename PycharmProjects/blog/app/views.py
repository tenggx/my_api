from django.shortcuts import render
from django.http import HttpResponse
from app.models import Article
# Create your views here.


def hello_world(request):
    return HttpResponse("Hello World")


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title:%s, brief_content:%s, conent:%s, article_id:%s, publish_date=%s' %(title, brief_content, content, article_id, publish_date)
    return HttpResponse(return_str)