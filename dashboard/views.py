from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')

def docteur(request):
    return render(request,'home.html')

def patient(request):
    return render(request,'home.html')

def message(request):
    return render(request,'home.html') 

def rendezvous(request):
    return render(request,'appointement.html')
