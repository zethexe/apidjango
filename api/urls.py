# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'clasificacion', views.ClasificacionViewSet)
router.register(r'genero', views.GeneroViewSet)
router.register(r'actor', views.ActorViewSet)
router.register(r'director', views.DirectorViewSet)
router.register(r'peliculas', views.PeliculaViewSet)
router.register(r'reparto', views.RepartoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]