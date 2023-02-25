from django.contrib import admin
from django.urls import path
from django.urls import re_path,include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^',include('Credit.urls')),
    path('',views.index, name='index')
]
