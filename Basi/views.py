
import imp
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from models import Busi
from django.views.generic import DeleteView

# Create your views here.

def home(request):
    
    if request.user.is_authenticated:
        if request.user.is_passenger:
            return redirect(reverse_lazy('users:passenger'))
        else:
            return redirect('users:driver')
    return render(request, "home.html")

def index(request):
    
    return render(request, "index.html")

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