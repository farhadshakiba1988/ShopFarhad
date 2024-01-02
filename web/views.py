from django.shortcuts import render


def ui_apps(request):
    return render(request, 'ui-apps.html')


def product_home(request):
    return render(request, 'ui-app-products-home.html')


def base(request):
    return render(request, 'index.html')


def products_category(request):
    return render(request, 'ui-app-products-category.html')


def ui_products(request):
    return render(request, 'ui-app-products-grid2col.html')
