from . import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'forumlist'

urlpatterns = [
    url(r'^$',views.PostPage.as_view(),name="hw"),
    url(r'^postapi/',views.PostList.as_view()),
    url(r'^(?P<post_id>[0-9])+', views.PostDetail.as_view(), name = 'detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)