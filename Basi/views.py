from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import ContactUs
# Create your views here.

def home(request):
    """[home view]

    Args:
        request ([function]): [view function to handle homepage based on user authorization levels]

    Returns:
        [template]: [return homepage template]
    """
    if request.user.is_authenticated:
        if request.user.is_passenger:
            return redirect(reverse_lazy('users:passenger'))
        else:
            return redirect('users:driver')
    return render(request, "home/home.html")

def index(request):
    """[summary]

    Args:
        request ([type]): [description]
    """
    return render(request, "home/index.html")
def about(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('Basi:success')
    return render(request, "home/about.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
