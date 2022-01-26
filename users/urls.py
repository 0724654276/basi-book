from django.urls import path
from . import views
app_name = "users"
urlpatterns = [

    path("passenger", views.passenger, name="passenger"),
    path("driver", views.driver, name="driver"),
    #path("", views.home, name="home")
    path("buspage", views.buspage, name="buspage"),
    path('deletebus/<int:pk>/', views.deleteBus, name='deletebus'),
]