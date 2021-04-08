from rest_framework import viewsets

from .serializers import ClasificacionSerializer
from .serializers import GeneroSerializer
from .serializers import ActorSerializer
from .serializers import DirectorSerializer
from .serializers import PeliculaSerializer
from .serializers import RepartoSerializer
from .models import Clasificacion
from .models import Genero
from .models import Actor
from .models import Director
from .models import Peliculas
from .models import Reparto


class ClasificacionViewSet(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all().order_by('id')
    serializer_class = ClasificacionSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all().order_by('id')
    serializer_class = GeneroSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all().order_by('id')
    serializer_class = ActorSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all().order_by('id')
    serializer_class = DirectorSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Peliculas.objects.all().order_by('id')
    serializer_class = PeliculaSerializer

class RepartoViewSet(viewsets.ModelViewSet):
    queryset = Reparto.objects.all().order_by('id')
    serializer_class = RepartoSerializer
