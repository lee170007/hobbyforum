from . import views
from django.conf.urls import url, include

app_name = 'member'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # member/listing
    url(r'^listing/$', views.ListingFormView.as_view(), name = 'listing'),
    # member/memberapi
    url(r'^api/', views.MemberList.as_view()),
]