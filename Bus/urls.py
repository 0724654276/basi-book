"""Bus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views
from django.conf import settings
from django.conf.urls.static import static
from mpesa.urls import mpesa_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("users.urls", namespace="users")),
    path('mpesa/', include(mpesa_urls)),
    #path("", include("mpesa_api", namespace="mpesa_api")),
    path('api/v1/', include('mpesa_api.urls', namespace="mpesa_api")),
    path("", include("Basi.urls", namespace="Basi")),
    path("", include("profileApp.urls", namespace="profileApp")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/driver/', views.DriverSignUpView.as_view(), name='driver_signup'),
    path('accounts/signup/customer/', views.PassengerSignUpView.as_view(), name='passenger_signup'),
    path("", include("blog.urls", namespace="blog")),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
    
if settings.DEBUG:
    urlpatterns+= static(
    settings.STATIC_URL, 
    document_root = settings.STATIC_ROOT)   