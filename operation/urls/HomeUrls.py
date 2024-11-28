from django.urls import path
from operation.views.Registerview import Homeview


app_name = 'operation'

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
]
