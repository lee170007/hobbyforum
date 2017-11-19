from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^login/',views.usrlogin,name="usrlogin"),
]