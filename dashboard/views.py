from django.shortcuts import render
from django.shortcuts import get_object_or_404,render,redirect
from .models import Docteur,Patient,Hopital

# Create your views here.


def home(request):
    if request.session.has_key('email_admin'):
        doc = get_object_or_404(Docteur,email=request.session['email_admin'])
        patient = Patient.objects.all()
        docteur = Docteur.objects.all()
        hopital = Hopital.objects.all()
        liste = {
            'user':doc,
            'patient':patient,
            'docteur':docteur,
            'hopital':hopital,
        }
        return render(request,'home.html',liste)
    else:
        return    render(request,'login/index.html') 

def ajouter_docteur(request):
    return render(request,'dashboard__doctors-add.html')


def lister_docteur(request):
    if request.session.has_key('email_admin'):
        doc = get_object_or_404(Docteur,email=request.session['email_admin'])
        patient = Patient.objects.all()
        docteur = Docteur.objects.all()
        hopital = Hopital.objects.all()
        liste = {
            'user':doc,
            'patient':patient,
            'docteur':docteur,
            'hopital':hopital,
        }
        return render(request,'dashboard__doctors.html',liste)
    else:
        return    render(request,'login/index.html') 
        



def ajouter_patient(request):
    if request.session.has_key('email_admin'):
        doc = get_object_or_404(Docteur,email=request.session['email_admin'])
        docteur = Docteur.objects.all()
        patient = Patient.objects.all()
        hopital = Hopital.objects.all()
        liste= {
            'user':doc,
            'patient':patient,
            'docteur':docteur,
            'hopital':hopital,
        }
        return render(request,'dashboard__patients-add.html',liste)
    else:
        return    render(request,'login/index.html')
    

def profil_patient(request):
    if request.session.has_key('email_admin'):
        doc = get_object_or_404(Docteur,email=request.session['email_admin'])
        patient = Patient.objects.all()
        docteur = Docteur.objects.all()
        hopital = Hopital.objects.all()
        liste = {
            'user':doc,
            'patient':patient,
            'docteur':docteur,
            'hopital':hopital,
        }
        return render(request,'dashboard__patient.html',liste)
    else:
        return    render(request,'login/index.html')
    

def lister_patient(request):
    if request.session.has_key('email_admin'):
        doc = get_object_or_404(Docteur,email=request.session['email_admin'])
        patient = Patient.objects.all()
        docteur = Docteur.objects.all()
        hopital = Hopital.objects.all()
        liste = {
            'user':doc,
            'patient':patient,
            'docteur':docteur,
            'hopital':hopital,
        }
        return render(request,'dashboard__patients.html',liste)
    else:
        return    render(request,'login/index.html')


def message(request):
    
    return render(request,'home.html') 

def rendezvous(request):
    return render(request,'appointement.html')


def login(request):
    if not request.session.has_key('email_admin'):
        if request.method == 'POST':
            m =  Docteur.objects.filter(email=request.POST['username'])
            if m.count() != 0 :
                erreur ="false"
                user = Docteur.objects.get(email=request.POST['username'])
                request.session['email_admin'] = user.email 
        # request.session['image_admin'] = user.PhotoDocteur 
                liste = {
                'erreur':erreur,
                'user':user,
                #'image_admin':request.session['image_admin']
                            }
                return  redirect('/',liste)
            else:           
                return  render(request,"login/index.html",{'erreur':"Mot de passe ou Non Utilisateur Incorrect Vous essayez de vous connecter en tant que Docteur"})
        return render(request,"login/index.html")
    else :
        return redirect("/")

def logout(request):
    if request.session.has_key('email_admin'):
        del  request.session['email_admin']
        return redirect("/login")   
    else: 
        return redirect("/")        