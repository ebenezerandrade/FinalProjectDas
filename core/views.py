from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
    #return render(request, '/home/ebenezer/DAS/projectDas/core/templates/index.html')

def contact(request):
	return render(resquest, 'contact.html')
	#return render(resquest, '/home/ebenezer/DAS/projectDas/core/templates/contact.html')
