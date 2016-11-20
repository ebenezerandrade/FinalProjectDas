from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, '/home/ebenezer/DAS/projectDas/core/templates/index.html', {'usuario':'Ebenezer'})