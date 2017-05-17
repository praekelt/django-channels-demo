from django.conf.urls import url
from demo.views import user_list, log_in, log_out, signup


urlpatterns = [
    url(r'^$', user_list, name='user_list'),
    url(r'^login/$', log_in, name='login'),
    url(r'^logout/$', log_out, name='logout'),
    url(r'^signup/$', signup, name='signup'),
]
