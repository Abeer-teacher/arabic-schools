from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from lessons.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية (السوداء)
    path('', lambda request: render(request, 'index.html')),

    # صفحة الدرس
    path('lesson/', home),
]