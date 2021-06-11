from django.db import models
from django.utils import timezone
# Create your models here.


#hopital 
class Hopital(models.Model): 
    NomHopital = models.CharField(default="",max_length=50)
    tel = models.CharField(default="",max_length=50) 
    Bp = models.CharField(default="",max_length=50) 

    def __str__(self):
        return  self.NomHopital

class Patient(models.Model):
    option = (
        ('francais','francais'),
        ('anglais','anglais')
    )
    genre = (
        ('feminin','feminin'),
        ('masculin','masculin') 
    )
    Nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField( max_length=50)
    genre = models.CharField(choices=genre, max_length=50)
    nationalite = models.CharField( max_length=50,default="")
    photo = models.CharField( max_length=50,default="default.png")
    adresse = models.CharField(default="", max_length=50)
    datenaissance = models.DateField(auto_now=False, auto_now_add=False)
    langue  = models.CharField(default="",max_length=50)
    def __str__(self):
        return   "Patient :  %s" % self.Nom

    
class Docteur(models.Model):
    option = (
        ('francais','francais'),
        ('anglais','anglais')
    )
    genre = (
        ('feminin','feminin'),
        ('masculin','masculin') 
    )
    Nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    genre = models.CharField(choices=genre, max_length=50)
    adresse = models.CharField(default="", max_length=50)
    specialisation = models.CharField(default="radiology", max_length=50)
    nationalite = models.CharField( max_length=50,default="")
    photo = models.CharField( max_length=50,default="default.png")
    datenaissance = models.DateField(auto_now=False, auto_now_add=False)
    langue  = models.CharField(default="", max_length=50)
    
   
    def __str__(self):
        return  "Docteur :  %s" %  self.Nom

class rendezvous(models.Model):

    examin = (
        ('Abdominal radiology','Abdominal radiology'),
        ('Breast imaging','Breast imaging'),
        ('Cardiothoracic radiology','Cardiothoracic radiology'),
        ('Cardiovascular radiology','Cardiovascular radiology')
    )
    NomPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    TypeExamin = models.CharField(choices=examin,max_length=50)
    NomDocteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
    Notes = models.TextField(max_length=50) 
    Lieu =models.CharField( max_length=50,default="clinic")
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return   "Rendevez vous pour  :  %s" % self.NomPatient

class Prescription(models.Model):

    examin = (
        ('paracetamol','Paracetamol'),
        ('Nivakine','Nivakine'),
        ('Amodiakine','Amodiakine')
      
    )
    NomPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Medication = models.CharField(choices=examin,max_length=50)
    NomDocteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
    Notes = models.TextField(max_length=50) 
    date = models.CharField(default="",max_length=200)
    def __str__(self):
        return   "Prescription de  :  %s" % self.Medication



class Rapport(models.Model):

    examin = (
        ('rapport activite','rapport activite'),
        ('rapport sur les maladies','rapport sur les maladies')
        
      
    )
    
    NomPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    TypeRapport = models.CharField(choices=examin,max_length=50)    
    NomDocteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
    Notes = models.TextField(max_length=50) 
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return   "rapport pour :  %s" % self.NomPatient

class Message(models.Model):
    nomexpediteur = models.CharField(default="abdoul",max_length=50)
    destinataire = models.EmailField(default="bellofidele@gmail.com",blank=False)
    subject = models.CharField(default="rien",max_length=200)
    contenu = models.TextField(default="salutation",blank=True)
    dateEnvoi = models.DateTimeField(default=timezone.now)
    
    lus = models.CharField(default="non",max_length=10)
    def __str__(self):
        return "Message envoyer à :  %s" % self.destinataire


class info_medicale(models.Model):
    NomPatient = models.ForeignKey(Patient, on_delete=models.CASCADE) 
    principale = models.CharField(default="",max_length=50)
    secondaire = models.CharField(default="",max_length=50)
    hopital = models.CharField(default="",max_length=200)
    observation = models.TextField(default="RAS",blank=True)
    periode = models.CharField(default="",max_length=200) 
    def __str__(self):
        return "info medicale du  :  %s" % self.NomPatient
