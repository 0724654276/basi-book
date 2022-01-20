from django import forms
from django.forms.widgets import EmailInput, NumberInput, TextInput, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


#usersignup form
class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100,help_text='Required')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
class UserUpdateForm(forms.ModelForm):
             class Meta:
                 model=User
                 fields = ['username','email','first_name','last_name']                
       
