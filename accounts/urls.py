from django.urls import path, include
from django.contrib.auth import views as auth_views
from simplemooc.accounts import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
]
