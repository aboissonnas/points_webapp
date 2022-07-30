from datetime import datetime

from django import forms


class AddForm(forms.Form):
    payer = forms.CharField(max_length=100, widget=forms.TextInput)
    points = forms.IntegerField(widget=forms.NumberInput)
    timestamp = forms.DateTimeField(
        widget=forms.DateTimeInput,
        initial=datetime.today(),
    )


class SpendForm(forms.Form):
    points = forms.IntegerField(widget=forms.NumberInput)