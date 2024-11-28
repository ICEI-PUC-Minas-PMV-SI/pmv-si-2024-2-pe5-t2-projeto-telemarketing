from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from operation.models.operationdb import Clientelemarketing
from django.urls import reverse_lazy
from operation.forms.reservationform import ReservationForm


class EditClientView(LoginRequiredMixin, UpdateView):
    model = Clientelemarketing
    template_name = "template_operation/create_client.html"
    form_class = ReservationForm
    success_url = reverse_lazy("listable:client")
