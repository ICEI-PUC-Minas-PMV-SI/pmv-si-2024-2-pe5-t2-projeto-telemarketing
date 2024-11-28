from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from operation.models.operationdb import Clientelemarketing

class ClientListView(LoginRequiredMixin, ListView):
    model = Clientelemarketing
    template_name = 'template_operation/list_client.html'
    context_object_name = 'clients'