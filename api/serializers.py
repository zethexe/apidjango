from rest_framework import serializers

from .models import Clasificacion
from .models import Genero
from .models import Actor
from .models import Director
from .models import Peliculas
from .models import Reparto

class ClasificacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clasificacion
        fields = ('name', 'description')

class GeneroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genero
        fields = ('id','description')

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', 'nationality')

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ('name', 'nationality')

class PeliculaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peliculas
        fields = ('title', 'duration','sinopsis','datelaunch','clasification','genre','director')

class RepartoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reparto
        fields = ('character', 'actor', 'movie')