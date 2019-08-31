from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from superanota.views import home

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^home$', home, name="home"),
    url(r'/$', home),
    url(r'$', home),
]
