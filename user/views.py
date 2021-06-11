from io import StringIO
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import  Administrateur


# Create your views here.
#page de connexion
def login(request):  
        if request.method == 'POST':
                m =  Administrateur.objects.filter(email=request.POST['username'],PwdAdministrateur=request.POST['password'])
                if m.count() != 0 :
                    erreur ="false"
                    user = Administrateur.objects.get(email=request.POST['username'])
                    request.session['email_admin'] = user.email 
                   # request.session['image_admin'] = user.PhotoAdministrateur 
                    for obj in m: 
                        obj.actif = "oui"
                        obj.save()
                    liste = {
                        'erreur':erreur,
                        #'image_admin':request.session['image_admin']
                        }
                    return  redirect('/Administrateur',liste)
                else:           
                    erreur ="Mot de passe ou Non Utilisateur Incorrect Vous essayez de vous connecter en tant que Administrateur"
                    return  render(request,"login/index.html",{'erreur':erreur})   

        
#inscription 
def inscription(request):
         if request.method == "POST":         
            m =  Administrateur.objects.filter(email=request.POST['nom'])
            if m.count() == 0 :          
                    email = request.POST['email']
                    Pwd = request.POST['Pwd']
                    PhotoAdministrateur = "default.jpg"
                    if request.POST['file']:
                        PhotoAdministrateur = request.POST['file']         
                    NomAdministrateur = request.POST['nom']
                    tel = request.POST['tel']
                    request.session["nom"] = email
                    Etud = Administrateur(email=email,NomAdministrateur=NomAdministrateur,Pwd=Pwd,PhotoAdministrateur=PhotoAdministrateur,tel=tel)
                    Etud.save()                   
                    #send_mail( 'activation', 'active ton compte.', 'bellofidele@gmail.com', 'bellofidele@gmail.com')
                    return redirect("/") 
                 
            else :
                    erreur ="Mot de passe ou Non Utilisateur Incorrect"
                    return  render(request,"login/index.html",{'erreur':erreur}) 
         return HttpResponse('error entrez') 
            
