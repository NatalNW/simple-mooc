from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('edit', views.edit, name='edit'),
    path('edit-passwd', views.edit_passwd, name='edit-passwd'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
    path('register/', views.register, name='register'),
]
