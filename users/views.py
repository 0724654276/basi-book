from django.shortcuts import render

from django.http import HttpResponse
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
from .forms import  DriverSignUpForm,PassengerSignUpForm,BusForm
from .models import  Driver, User,Passenger,Bus
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


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
    user_profile = Bus.objects.all()
    if request.method == 'POST':
        print("Hello")
        form = BusForm(request.POST,request.FILES)
        if form.is_valid():
            print("Is valid")
            new_bus = form.save(commit = False)
            #new_proj.user = user_profile
            new_bus.save()
           
            print(new_bus.__dict__)
        return redirect('users:driver')  
    else:
        form = BusForm()
    return render(request,'drivers/driver.html',{'form':form})    

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
        kwargs['user_type'] = 'passenger'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:passenger')


def passenger(request):
    """[passenger main view]

    Args:
        request ([function]): [main passenger view]

    Returns:
        [template]: [render customer page]
    """
    context = {
        "bus": Bus.objects.all()
    }
    return render(request, "passengers/passenger.html", context)

def buspage(request):
    context = {
        "bus":Bus.objects.all()
    }
    return render(request, "drivers/businfo.html",context)

@login_required(login_url='login')
def deletebus(request, id):
    """bus = Bus.objects.get(id=pk)

    if request.user != bus.user:
        return HttpResponse('You are not allowed')

    if request.method == 'POST':
        bus.delete()
        return redirect('Basi:index')
        """
    bus = Bus.objects.get(id=id)
    print("got id")
    if request.method == "GET":
        print("got post")
        bus.delete()
        return redirect("users:buspage")
    context = {
        "bus": bus
    }
    return render(request, 'drivers/driver.html', context)
@login_required(login_url='login')
def updatebus(request, pk):
    bus = Bus.objects.get(id=pk)
    form = BusForm(instance=bus)

    if request.user != bus.user:
        return HttpResponse('You are not allowed')

    if request.method == 'POST':
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            return redirect('users:buspage')
    context = {
        'form':form
    }
    return render(request, 'drivers/bus_form.html', context)
