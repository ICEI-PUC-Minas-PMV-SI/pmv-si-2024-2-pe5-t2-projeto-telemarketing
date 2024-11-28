from django.urls import path
from operation.views.Registerclient import CreateNewClient


app_name = 'create'

urlpatterns = [
    path('client/', CreateNewClient.as_view(), name='newclient'),
]
