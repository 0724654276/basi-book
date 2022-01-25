from django.shortcuts import render
import requests
from .models import Bus

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def findbus(request):
    context = {}
    if request.method == 'POST':
        terminus_r = request.POST.get('terminus')
        route_r = request.POST.get('route')
        date_r = request.POST.get('date')
        Bus_list = Bus.objects.filter(terminus=terminus_r, route=route_r, date=date_r)
        if Bus_list:
             return render(request, 'list.html', locals())
        else:
            context["error"] = "Sorry no buses available"
            return render(request, 'findbus.html', context)
    else:
        return render(request, 'findbus.html')        