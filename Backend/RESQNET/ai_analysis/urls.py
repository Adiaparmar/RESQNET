from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_test, name='home_test'),
]