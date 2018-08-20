from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^myadmin/', include('myadmin.urls')),
    url(r'^', include('myweb.urls')),

]
