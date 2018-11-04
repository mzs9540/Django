from django.urls import path

from myfirst_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
