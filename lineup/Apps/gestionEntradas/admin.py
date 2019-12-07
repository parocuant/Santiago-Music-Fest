from django.contrib import admin
 
from lineup.Apps.gestionEntradas.models import Entrada,Escenario,Artista

# Register your models here.

admin.site.register(Entrada)
admin.site.register(Escenario)
admin.site.register(Artista)
