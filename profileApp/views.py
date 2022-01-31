from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .forms import UserUpdateForm, ProfileUpdateForm
from users.models import Bus
from .models import Profile
from users.models import User
# Create your views here.

# Update it here
@login_required
def profile(request):
    bus = Bus.objects.all()
    user_buses = Bus.objects.filter(user=request.user).order_by('-date_posted')
    paginator=Paginator(user_buses,2)    #2 per page
    page=request.GET.get('page')        #Page requested in the previous paragraph,For example, click'next page',This page takes variables as'page'express
    try:
      bus_obj=paginator.page(page) #Gets the number of pages requested by the front end
    except PageNotAnInteger:
        bus_obj=paginator.page(1)   #If the front-end input is not a number,Just go back to page one
    except EmptyPage:
        bus_obj=paginator.page(paginator.num_pages)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('Basi:index')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'bus': bus,
        'user_buses' : user_buses,
        "user_list" : bus_obj
    }

    return render(request, 'profile.html', context)


