from django.urls import path
from . import views
app_name = "profileApp"
urlpatterns = [
       path('profile/', views.profile, name='profile'),
       path("all_profiles/",views.all_profiles, name="all_profiles"),
       path('user_profile/<username>/', views.user_profile, name='user_profile'),
]