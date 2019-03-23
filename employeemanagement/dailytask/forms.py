from django import forms
from .models import Dailytask
class DailytaskForm(forms.Form):
    date=forms.DateField()
    workingproject=forms.CharField()
    company=forms.CharField()
    workinghour=forms.DecimalField()
    stage=forms.CharField()      