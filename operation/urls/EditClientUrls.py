from django.urls import path
from operation.views.EditClient import EditClientView


app_name = 'edit'

urlpatterns = [
    path('client/<int:pk>/', EditClientView.as_view(), name='client'),
]
