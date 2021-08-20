from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from accounts.forms import RegisterForm


@login_required
def dashboard(req):
    template_name = 'profile.html'
    return render(req, template_name)


def register(req):
    template_name = 'register.html'

    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                                password=form.cleaned_data['password1'])
            login(req, user)
            return redirect('core:home')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(req, template_name, context)
