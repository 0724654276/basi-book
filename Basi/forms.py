from django import forms
from .models import  Ticket
class BusForm(forms.ModelForm):
    """
    model form to post bus
    Args:
        forms (model): [class to help in creating the model form]
    """
    class Meta:
        model = Ticket
        fields = "__all__"

from .models import ContactUs

from django.forms import ModelForm
class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
