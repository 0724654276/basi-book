from django import forms

class Ticketform(forms.ModelForm):
    """
    model form to book a bus
    Args:
        forms (model): [class to help in creating the model form]
    """
    class Meta:
        model = Ticket
        fields = "__all__"
        