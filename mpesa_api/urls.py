from django.urls import path, include
from . import views
app_name = "mpesa_api"
urlpatterns = [
    path('', views.home, name='home'),
    # path('daraja/stk-push', views.stk_push_callback, name='mpesa_stk_push_callback'),
    # path('daraja/c2b', views.c2b_callback, name='c2b_callback'),
    path('payment/', views.payment, name='payment'),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
]