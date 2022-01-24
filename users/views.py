from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from .forms import  DriverSignUpForm
from .models import  Driver, User,Passenger


class DriverSignUpView(CreateView):
    """
    class based view to handle driver signup
    """
    model = User
    form_class = DriverSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'driver'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:driver')

def driver(request):
    """
    function to handle to driver page
    """
    current_user = request.user
    return render(request,'driver/driver.html')    

