from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    email = forms.EmailField(label='E-mail') 

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email already being used!')
        
        return email

    def save(self):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()

        return user