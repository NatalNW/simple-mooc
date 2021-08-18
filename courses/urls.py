from django.urls import path
from courses import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.details, name='details'),
]