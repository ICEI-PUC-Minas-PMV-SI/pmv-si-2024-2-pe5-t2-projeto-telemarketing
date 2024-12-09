from django.urls import path
from operation.views.Listclient import ClientListView

app_name = 'listable'

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client'),
]
