from django.urls import path
from . import views
from django.contrib import admin



urlpatterns = [
    
    path('', views.bridge_list, name='bridge_list'),
    path('bridge/<int:pk>/brick/new/', views.brick_new, name='brick_new'),
    path('bridge/<int:pk>/', views.brick_list, name='brick_list'),
    path('bridge/new/', views.bridge_new, name='bridge_new'),
]

