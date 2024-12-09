from django.views.generic import TemplateView


class Homeview(TemplateView):
    """
    Class Based View que renderiza a página index.html
    """
    template_name = 'home/home.html'

# def home_view(request):
#     return HttpResponse('<h1>Olá Mundo!!!</h1>')
