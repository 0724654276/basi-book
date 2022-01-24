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
from .forms import  DriverSignUpForm,PassengerSignUpForm
from .models import  Driver, User,Passenger


class DriverSignUpView(CreateView):
    """[class view]

    Args:
        CreateView ([class]): [class based view to handle driver signup]

    Returns:
        [method]: [method to redirect user[driver] to driver page if form is valid]
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
    """[driver view]

    Args:
        request ([function]): [handle main driver/owner view]

    Returns:
        [template]: [render a template[driver]]
    """
    current_user = request.user
    return render(request,'driver/driver.html')    

class PassengerSignUpView(CreateView):
    """[class view]

    Args:
        CreateView ([class]): [class based view to handle passenger signup]

    Returns:
        [method]: [redirect user to passenger page if form is valid otherwise to the form it is]
    """
    model = User
    form_class = PassengerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:customer')


def passenger(request):
    """[passenger main view]

    Args:
        request ([function]): [main passenger view]

    Returns:
        [template]: [render customer page]
    """
    return render(request, "customer/customer.html", context)

