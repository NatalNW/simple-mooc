from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    email = forms.EmailField(label='E-mail') 

    def save(self):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()

        return user