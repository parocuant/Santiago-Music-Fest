from django.shortcuts import render
from .models import Entrada, Escenario, Artista
from django.views import generic

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_artistas=Artista.objects.all().count()
    num_escenarios=Escenario.objects.all().count()
    """
    # Libros disponibles (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # El 'all()' esta implícito por defecto.
    """
    return render(
        request,
        'index.html',
        context={'num_artistas':num_artistas,'num_escenarios':num_escenarios},
    )

def lineup(request):
    num_artistas=Artista.objects.all().count()
    num_escenarios=Escenario.objects.all().count()
    return render(
        request,
        'lineup.html',
        context={'num_artistas':num_artistas,'num_escenarios':num_escenarios},
    )

def stages(request):
    num_artistas=Artista.objects.all().count()
    num_escenarios=Escenario.objects.all().count()
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'stages.html',
        context={'num_artistas':num_artistas,'num_escenarios':num_escenarios},
    )

class EventNumbers(generic.ListView):
    context_object_name = 'artista_list'
    queryset = Artista.objects.all()
    template_name = 'lineup.html'
    def get_context_data(self, **kwargs):
        context = super(EventNumbers, self).get_context_data(**kwargs)
        context['escenario_list'] = Escenario.objects.all()
        return context


class ArtistaList(generic.ListView):
    template_name= 'index.html'
    def get_queryset(self):
        return Artista.objects.all()
