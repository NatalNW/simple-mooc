from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'user': 'Drougras'})

def contact(request):
    return render(request, 'contact.html')