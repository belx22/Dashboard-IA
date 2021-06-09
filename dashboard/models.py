from django.db import models
from django.utils import timezone
# Create your models here.

class Patient(models.Model):
    option = (
        ('francais','francais'),
        ('anglais','anglais')
    )
    Nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField( max_length=50)
    genre = models.CharField( max_length=50)
    datenaissance = models.DateField(auto_now=False, auto_now_add=False)
    langue  = models.CharField(choices=option, max_length=50)
    
class Docteur(models.Model):
    option = (
        ('francais','francais'),
        ('anglais','anglais')
    )
    Nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    genre = models.CharField( max_length=50)
    datenaissance = models.DateField(auto_now=False, auto_now_add=False)
    langue  = models.CharField(choices=option, max_length=50)
    def __str__(self):
        return  self.Nom

class rendezvous(models.Model):

    examin = (
        ('Abdominal radiology','Abdominal radiology'),
        ('Breast imaging','Breast imaging'),
        ('Cardiothoracic radiology','Cardiothoracic radiology'),
        ('Cardiovascular radiology','Cardiovascular radiology')
    )
    NomPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    TypeExamin = models.CharField(max_length=50)
    NomDocteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
    Notes = models.TextField(max_length=50) 
    Lieu = models.CharField(max_length=50) 
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return  self.NomPatient

class Prescription(models.Model):

    examin = (
        ('paracetamol','Paracetamol'),
        ('Nivakine','Nivakine'),
        ('Amodiakine','Amodiakine')
      
    )
    NomPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Medication = models.CharField(max_length=50)
    NomDocteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
    Notes = models.TextField(max_length=50) 
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return  self.NomDocteur



class Rapport(models.Model):

    examin = (
        ('rapport activite','rapport activite'),
        ('rapport maladie','rapport maladie')
        
      
    )
    NomPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    TypeRapport = models.CharField(max_length=50)
    NomDocteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
    Notes = models.TextField(max_length=50) 
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return  self.TypeRapport

class Message(models.Model):
    expediteur =  models.EmailField(default="belx22@gmail.com",blank=False) 
    nomexpediteur = models.CharField(default="abdoul",max_length=50)
    destinataire = models.EmailField(default="bellofidele@gmail.com",blank=False)
    subject = models.CharField(default="rien",max_length=200)
    contenu = models.TextField(default="salutation",blank=True)
    dateEnvoi = models.DateTimeField(default=timezone.now)
    atachement = models.FileField(default="img.jpg")
    lus = models.CharField(default="non",max_length=10)
    def __str__(self):
        return "Message envoyer à :  %s" % self.destinataire
