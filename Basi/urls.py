from django.urls import path
from . import views
app_name = "Basi"
urlpatterns = [
   
    path("home", views.home, name="home"),
    path("", views.index, name="index"),
    path("book", views.book, name="book"),
    path("about", views.about, name="about"),
]