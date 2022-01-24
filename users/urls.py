from django.urls import path
from . import views
app_name = "users"
urlpatterns = [
    path("", views.home, name="home"),
    path("customer", views.customer, name="customer"),
    path("driver", views.driver, name="driver"),
    
]