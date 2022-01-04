from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from accounts.forms import RegisterForm, EditAccountForm


@login_required
def dashboard(req):
    template_name = 'dashboard.html'
    return render(req, template_name)


@login_required
def edit(req):
    template_name = 'edit-profile.html'
    context = {}
    
    if req.method == 'POST':
        form = EditAccountForm(req.POST, instance=req.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=req.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=req.user)

    context['form'] = form

    return render(req, template_name, context)

@login_required
def edit_passwd(req):
    template_name = 'edit-passwd.html'
    context = {}

    if req.method == 'POST':
        form = PasswordChangeForm(data=req.POST, user=req.user)

        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=req.POST)
    
    context['form'] = form
    return render(req, template_name, context)


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
