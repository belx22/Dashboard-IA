from django.db import models
from django.utils import timezone

# Create your models here.

#table Administrateur
class Administrateur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True,blank="true")
    PwdAdministrateur = models.CharField(max_length=15,blank="true")  
    PhotoAdministrateur = models.ImageField(default="image.png")
    actif = models.CharField(default='oui',max_length=3)
    
    def __str__(self):
        return self.nom
    
