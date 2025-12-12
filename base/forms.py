from django import forms
from .models import Submission,User
from django.contrib.auth.forms import UserCreationForm



class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
       
        exclude=['participant','event']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email','password1','password2']