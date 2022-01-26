from django import forms
from models import Bus
class BusForm(forms.ModelForm):
    """
    model form to post bus
    Args:
        forms (model): [class to help in creating the model form]
    """
    class Meta:
        model = Bus
        fields = "__all__"