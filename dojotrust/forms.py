from django import forms
from .models import Business,Users

class Businessform(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['user','users']
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Users
        exclude=['user']
