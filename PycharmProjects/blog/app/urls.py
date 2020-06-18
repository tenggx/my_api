from django.conf.urls import url
from .views import hello_world, article_content


urlpatterns = [
    url(r'^hello_world/',hello_world),
    url(r'^content/',article_content),
]