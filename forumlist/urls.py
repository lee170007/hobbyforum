from . import views
from django.conf.urls import url, include

app_name = 'forumlist'

urlpatterns = [
    url(r'^$',views.PostPage.as_view(),name="hw"),
    url(r'^(?P<post_id>[0-9])+', views.PostDetail.as_view(), name = 'detail'),
]