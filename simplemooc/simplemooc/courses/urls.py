from django.urls import path
from simplemooc.courses import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.details, name='details'),
]