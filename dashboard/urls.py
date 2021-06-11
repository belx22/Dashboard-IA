from django.urls import path
from . import views

app_name= "dashboard"
urlpatterns = [
    path('',views.home),
    path('Appointment',views.rendezvous,name="rendezvous"),
    path('Add_doctor',views.ajouter_docteur,name="ajout_docteur"),
    path('dashboard__doctors',views.lister_docteur,name="list_docteur"),  
    path('dashboard__patients-add',views.ajouter_patient),
    path('dashboard__patients',views.lister_patient),
    path('dashboard__patient',views.profil_patient),
    path('message',views.message),
]
