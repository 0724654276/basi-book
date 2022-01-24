from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.forms import TextInput
from .models import User,Driver,Passenger

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



