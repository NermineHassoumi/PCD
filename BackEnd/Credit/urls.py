from django.urls import re_path
from Credit import views

urlpatterns = [
    re_path(r'^demande$',views.demandeApi),
    re_path(r'^demande/([0-9]+)$',views.demandeApi)
]
