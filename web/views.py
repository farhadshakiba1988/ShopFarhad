from django.shortcuts import render


def home(request):
    return render(request, 'ui-apps.html')


def base(request):
    return render(request, 'index.html')
