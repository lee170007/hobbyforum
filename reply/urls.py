from django.conf.urls import url
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

from django.contrib.auth.views import login, logout

app_name = 'reply'

urlpatterns = [
	
	 url(r'^replyapi/',views.ReplyList.as_view()),
	 url(r'^(?P<post_id>[0-9])+', views.ReplyDetail.as_view(), name = 'addreply'),
  	 
  	 #url(r'^(?P<post_id>[0-9])+', views.AddReplyFormView.as_view(), name = 'addreply'),

]

urlpatterns = format_suffix_patterns(urlpatterns)