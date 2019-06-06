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
        widgets={
            'name': forms.TextInput(attrs={'placeholder':'Full names'}),
        }



class ReviewForm(forms.ModelForm):
    class Meta:
        model=Reviews
        exclude=['user','business','profile']
        widgets={
            'review': forms.TextInput(attrs={'placeholder':'Leave a review Press enter when done'}),
        }
