from django.urls import path
from calculation import views

urlpatterns = [
    path('', views.home, name = 'home' ),
    path('add', views.add, name = 'add' ),
    
]
