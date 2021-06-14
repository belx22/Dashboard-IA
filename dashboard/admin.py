from django.contrib import admin
from .models import Docteur,Patient,rendezvous,Prescription,Message,Rapport,info_medicale,Hopital,profil_sante
# Register your models here.
admin.site.register(Docteur)
admin.site.register(Patient)
admin.site.register(rendezvous)
admin.site.register(Prescription)
admin.site.register(Message)
admin.site.register(Rapport)
admin.site.register(info_medicale)
admin.site.register(Hopital)
admin.site.register(profil_sante)