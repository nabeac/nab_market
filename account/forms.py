from django import forms
from .models import User


class Signup(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
