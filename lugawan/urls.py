
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('macabalan/', views.macabalan, name='macabalan'),
    path('expense/', views.expenseview, name='expensepath'),
]
