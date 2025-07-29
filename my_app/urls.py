from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('write/', views.write_random_string, name='write'),
    path('read/', views.read_latest_string, name='read'),
]
