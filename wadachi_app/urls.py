from django.urls import path
from . import views

urlpatterns = [
    path('', views.bridge_list, name='bridge_list'),
    path('brick/new/', views.brick_new, name='brick_new'),
]


