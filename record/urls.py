from django.urls import path
from . import views

urlpatterns = [
    path('', views.record, name='record'),
    path('name/', views.name, name='name'),
    path('<str:name>/', views.greet, name='greet'),
    
]