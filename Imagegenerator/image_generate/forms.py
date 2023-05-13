from django.forms import ModelForm
from django import forms


class LogiChecker(forms.Form):
    userInput  = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': ' Enter your text here'}))
    output = forms.CharField(required=False , widget=forms.TextInput(attrs={'placeholder': ' Output'}))
