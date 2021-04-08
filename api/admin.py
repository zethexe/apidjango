from django.contrib import admin
from .models import Clasificacion
from .models import Genero
from .models import Actor
from .models import Director
from .models import Peliculas
from .models import Reparto

# Register your models here.
admin.site.register(Clasificacion)
admin.site.register(Genero)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Peliculas)
admin.site.register(Reparto)