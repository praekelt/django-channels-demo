from django.conf.urls import url
from demo.views import article_list


urlpatterns = [
    url(r"^$", article_list, name="article_list"),
]
