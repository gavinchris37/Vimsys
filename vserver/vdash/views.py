from django.http import HttpResponse
from django.shortcuts import render


def dashboard(request):
    return render(request, 'vdash/dashboard.html')


def dashboardviews(request, pk):
    return render(request, 'vdash/dashboardviews.html')
