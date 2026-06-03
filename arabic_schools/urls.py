from django.contrib import admin
from django.urls import path
from lessons.views import lesson

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', lesson, {'letter': 'ا'}),

    # باقي الحروف
    path('lesson/<str:letter>/', lesson),
]