from django.urls import path
from . import views
app_name = "Basi"
urlpatterns = [
   
    path("home", views.home, name="home"),
    path("", views.index, name="index"),
    #path("about", views.about, name="about"),
]