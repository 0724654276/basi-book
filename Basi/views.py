from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from .forms import ContactForm
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, 'home/contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'home/about.html', context)
