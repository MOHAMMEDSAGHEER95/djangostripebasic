__author__ = 'sayone'

from django.conf.urls import url

from django.urls import path

from . import views

urlpatterns = [
    path('charge/', views.charge, name='charge'), # new
    path('', views.HomePageView.as_view(), name='home'),
]