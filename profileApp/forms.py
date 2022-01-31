from django import forms
from users.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    """[user update form]

    Args:
        forms ([class form]): [update users]
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """[profile update]

    Args:
        forms ([class]): [form to update profile model]
    """
    class Meta:
        model = Profile
        fields = ['image']