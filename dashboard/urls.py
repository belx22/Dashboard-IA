from django.urls import path
from . import views

app_name= "dashboard"
urlpatterns = [
    path('',views.home),
    path('rendezvous',views.rendezvous,name="rendezvous"),
    path('docteur',views.docteur),
    path('patient',views.patient),
    path('message',views.message),
]
