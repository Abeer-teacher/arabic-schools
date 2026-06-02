from django.contrib import admin
from django.urls import path, include
from lessons import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 ده أهم سطر
    path('', views.lesson, {'letter': 'ب'}),

    path('lesson/<str:letter>/', views.lesson),
]