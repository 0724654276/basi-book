from django.shortcuts import render,get_object_or_404
from django.db.models import Q 
from django.conf import settings
from django.http import HttpResponse
from django.core.paginator import Paginator
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
from .forms import  DriverSignUpForm,PassengerSignUpForm,BusForm,BookingForm
from .models import  Driver, User,Passenger,Bus,Booking,Route
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
User = get_user_model()

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
        return redirect('users:buspage')  
    else:
        form = BusForm()
    return render(request,"drivers/driver.html",{'form':form})    

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


def bookForm(request):
    """[passengerbookform main view]

    Args:
        request ([function]): [main passenger view]

    Returns:
        [template]: [render customer page]
    """
    current_user = request.user
    busData = Bus.objects.all()
    buses = Booking.objects.all()
    if request.method == 'POST':
        print("Hello")
        form = BookingForm(request.POST,request.FILES)
        if form.is_valid():
            print("Is valid")
            new_order = form.save(commit = False)
            #new_proj.user = user_profile
            new_order.save()
            
            print(new_order.__dict__)
        return redirect('users:bookinfo')  
    else:
        form = BookingForm()

    return render(request,'passengers/bookform.html',{'form':form, "buses":buses, "busData":busData})    
def passenger(request):
    bus = Bus.objects.all()
    routes = Route.objects.all()
    
    
      
    return render(request, "passengers/passenger.html", {"routes":routes, "bus": bus,})

def selectedroute(request,id):
    routes = Route.objects.get(id=id)
    # print(route)
    return render(request,"passengers/selectedroute.html", {"routes":routes})

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


def bookinfo(request):
    current_user = request.user
    context = {
        "orders": Booking.objects.all(),
        "buses": Bus.objects.all()
    }
    return render(request, "passengers/bookinfo.html", context)






<<<<<<< HEAD
from django.shortcuts import render, redirect,get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

=======
>>>>>>> 8a9d08f8d9ff7fbb485b5190af1722cfdc3a46e6


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = get_user_model().objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "registration/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="registration/password//password_reset.html", context={"password_reset_form":password_reset_form})


