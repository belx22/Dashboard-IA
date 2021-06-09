from django.contrib import admin
from .models import Docteur,Patient,rendezvous,Prescription,Message,Rapport
# Register your models here.
admin.site.register(Docteur)
admin.site.register(Patient)
admin.site.register(rendezvous)
admin.site.register(Prescription)
admin.site.register(Message)
admin.site.register(Rapport)