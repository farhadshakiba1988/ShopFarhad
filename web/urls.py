from django.urls import path

from web import views

urlpatterns = [
    path('ui_apps/', views.ui_apps),
    path('', views.base),
    path('product_home/', views.product_home),
    path('ui_products/', views.ui_products),
    path('products_category/', views.products_category),
]
