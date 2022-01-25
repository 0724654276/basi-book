from django.urls import path, include
#from django.contrib.auth.views import LogoutView
from . import views



urlpatterns = [
    path('', views.home, name="home"),
      path('findbus', views.findbus, name="findbus"),
]