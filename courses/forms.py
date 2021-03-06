from django import forms
from django.conf import settings

from core.mail import send_mail_template


class ContactCourse(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def send_email(self, course):
        subject = f'{course} Contact'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        template_name = 'courses/contact_email.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )
