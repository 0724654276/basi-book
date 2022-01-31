from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.forms import TextInput
from .models import BookingModel, User,Driver,Passenger,BusModel

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
class PassengerSignUpForm(UserCreationForm):
    """[passenger form]

    Args:
        UserCreationForm ([models form]): [create a passenger sign up form]

    Returns:
        [class method]: [safe the user[passenger] form]
    """
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
            passenger = Passenger.objects.create(user=user)
        return user


class DriverSignUpForm(UserCreationForm):
    """[driver class]

    Args:
        UserCreationForm ([form]): [create a form from driver model class]

    Returns:
        [class method]: [method to safe the form]
    """
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver = True
        user.save()
        driver = Driver.objects.create(user=user)
        return user

class BusForm(forms.ModelForm):
    """
    model form to post bus
    Args:
        forms (model): [class to help in creating the model form]
    """
    class Meta:
        model = BusModel
        fields = "__all__"


class BookingForm(forms.Model):
    class Meta:
        model = BookingModel
        fields = '__all__'
        exclude = ['date_booked', 'user', 'bus']

