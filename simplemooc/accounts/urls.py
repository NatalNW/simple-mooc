from django.urls import path, include
from django.contrib.auth import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
]
