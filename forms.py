from django import forms
from . import models

class UserFeedback(forms.ModelForm):
    class Meta:
        model = models.UserFeedback
        fields = ['name', 'email','phone','message']
