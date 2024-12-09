from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from operation.forms.reservationform import ReservationForm
from operation.models.operationdb import Clientelemarketing


class CreateNewClient(LoginRequiredMixin, CreateView):
    template_name = "template_operation/create_client.html"
    model = Clientelemarketing
    form_class = ReservationForm
    success_url = reverse_lazy("listable:client")
