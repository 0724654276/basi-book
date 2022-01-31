from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this

app_name = "users"
urlpatterns = [

    path("passenger", views.passenger, name="passenger"),
    path("driver", views.driver, name="driver"),
    path('bookingRide/', views.bookingRide, name='bookingRide'),
    #path("", views.home, name="home")
    path("buspage/", views.buspage, name="buspage"),
    path('deletebus/<int:id>/', views.deletebus, name='deletebus'),
    path('updatebus/<int:pk>/', views.updatebus, name='updatebus'),
    path("bookinfo", views.bookinfo, name="bookinfo"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("bookform", views.bookForm, name="bookform"),
   
    
]