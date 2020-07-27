from django.urls import path
from . import views

urlpatterns = [
    path('', views.bridge_list, name='bridge_list'),
    path('brick/new/', views.brick_new, name='brick_new'),
    path('bridge/new/', views.bridge_new, name='bridge_new'),
    path('bridge/<int:pk>/', views.brick_list, name='brick_list'),
]

