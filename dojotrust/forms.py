from django import forms
from .models import Business,Users,Reviews

class Businessform(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['user','users']
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Users
        exclude=['user']


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Reviews
        exclude=['user','business','profile']
