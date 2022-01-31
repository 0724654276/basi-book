from django import forms
from models import  Ticket
class BusForm(forms.ModelForm):
    """
    model form to post bus
    Args:
        forms (model): [class to help in creating the model form]
    """
    class Meta:
        model = Ticket
        fields = "__all__"
