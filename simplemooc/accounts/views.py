from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

def register(req):
    template_name = 'register.html'

    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(req, template_name, context)

