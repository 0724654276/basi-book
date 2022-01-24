from django.urls import path
from . import views
app_name = "users"
urlpatterns = [

    path("passenger", views.passenger, name="passenger"),
    path("driver", views.driver, name="driver"),
    
]