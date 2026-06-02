from django.urls import path
from . import views

urlpatterns = [
    path('lesson/<str:letter>/', views.lesson),
]