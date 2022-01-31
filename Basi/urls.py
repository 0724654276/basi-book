from django.urls import path
from . import views
from .views import successView
app_name = "Basi"
urlpatterns = [
    path("home", views.home, name="home"),
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path('success/', successView, name='success'),
]