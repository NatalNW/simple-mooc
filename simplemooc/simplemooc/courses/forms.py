from django.core.mail import send_mail
from django.conf import settings
from django import forms

class ContactCourse(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def send_email(self, course):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        subject = f'{course} Contact'
        message = f'Name: {name};E-mail: {email};{message}'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])