from django import forms
from operation.models.operationdb import Clientelemarketing


class ReservationForm(forms.ModelForm):
    """
    Class that lets to create a Form class from a Django model
    """

    class Meta:
        model = Clientelemarketing
        fields = ['name', 'address', 'type_client', 'telcell', 'telfix', 'status']
