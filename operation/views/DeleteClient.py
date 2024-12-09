from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from operation.models.operationdb import Clientelemarketing


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """
    Class Based View to delete a reservation
    """
    model = Clientelemarketing
    success_url = "/"
    # context_object_name = 'registers'
    template_name = "template_operation/confirm_delete.html"
