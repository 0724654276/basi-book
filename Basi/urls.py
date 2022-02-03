from django.urls import path
from . import views
from .views import successView
app_name = "Basi"
urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.index, name="index"),
    path("book", views.book, name="book"),
    path("about", views.about, name="about"),
    path("routes", views.routes, name="routes"),
    path('success/', successView, name='success'),
]