from django.shortcuts import redirect, render
from django.conf import settings
from accounts.forms import RegisterForm


def register(req):
    template_name = 'register.html'

    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(req, template_name, context)
