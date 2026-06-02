from django.contrib import admin
from django.urls import path
from lessons import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', views.lesson, {'letter': 'ا'}),

    # كل الحروف
    path('lesson/<str:letter>/', views.lesson),
]