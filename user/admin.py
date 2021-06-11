from django.contrib import admin

# Register your models here.

from .models import   Administrateur
# Register your models here.
admin.site.site_header = "Gestion des utilisateurs"
admin.site.register(Administrateur)

