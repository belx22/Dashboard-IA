from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')

def ajouter_docteur(request):
    return render(request,'dashboard__doctors-add.html')


def lister_docteur(request):
    return render(request,'dashboard__doctors.html')


def ajouter_patient(request):
    return render(request,'dashboard__patients-add.html')

def profil_patient(request):
    return render(request,'dashboard__patient.html')

def lister_patient(request):
    return render(request,'dashboard__patients.html')


def message(request):
    return render(request,'home.html') 

def rendezvous(request):
    return render(request,'appointement.html')
