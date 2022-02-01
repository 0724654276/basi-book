from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from .models import Busi
from django.views.generic import DeleteView
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from .models import Ticket
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
    return render(request, "home.html")

def index(request):
    
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


def routes(request):
    return render(request, "routes.html")
class BusiDeleteView(DeleteView):
    model = Busi
    template_name = 'delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.name == Busi.name:
            return True
        else:
            return False
        return render(request, "home.html")

def index(request):
    """[summary]

    Args:
        request ([type]): [description]
    """
    return render(request, "index.html")
class TicketView():
    """
    view class to book a bus
    """
    model = Ticket
    fields = "__all__"
    template_name = 'ticket.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
def book(request):
    return render(request,"book.html")
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
