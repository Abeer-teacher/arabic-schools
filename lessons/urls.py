from django.urls import path
from . import views

urlpatterns = [
    path('', views.lesson, {'letter': 'ب'}),  # الصفحة الرئيسية
    path('lesson/<str:letter>/', views.lesson),
]