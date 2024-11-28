from django.urls import path
from operation.views.DeleteClient import ClientDeleteView


app_name = 'delete'

urlpatterns = [
    path('client/<int:pk>/', ClientDeleteView.as_view(), name='client'),
]
