from django.urls import path

from web import views

urlpatterns = [
    path('', views.home),
    path('/index', views.base),
]
