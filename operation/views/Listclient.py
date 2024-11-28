from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from operation.models.operationdb import Clientelemarketing


class ClientListView(LoginRequiredMixin, ListView):
    model = Clientelemarketing
    template_name = 'template_operation/list_client.html'
    context_object_name = 'clients'
