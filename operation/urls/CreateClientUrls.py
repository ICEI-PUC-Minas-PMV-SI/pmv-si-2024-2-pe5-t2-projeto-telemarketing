from django.urls import path
from operation.views.Registerview import Homeview
from operation.views.Registerclient import CreateNewClient


app_name = 'create'

urlpatterns = [
    path('', CreateNewClient.as_view(), name='newclient'),
]
