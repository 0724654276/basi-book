
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView

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
    return render(request, "index.html")
