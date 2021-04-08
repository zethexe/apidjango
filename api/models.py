from django.db import models

# Create your models here.
class Clasificacion(models.Model):
    name = models.TextField()
    description = models.TextField()
    def __str__(self):
        return self.name

class Genero(models.Model):
    description = models.TextField()
    def __str__(self):
        return self.description

class Actor(models.Model):
    name = models.TextField()
    nationality = models.TextField()
    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.TextField()
    nationality = models.TextField()
    def __str__(self):
        return self.name

class Peliculas(models.Model):
    title = models.TextField()
    duration = models.IntegerField()
    sinopsis = models.TextField()
    datelaunch = models.DateTimeField()
    clasification = models.ForeignKey("Clasificacion",on_delete=models.CASCADE)
    genre = models.ForeignKey("Genero",on_delete=models.CASCADE)
    director = models.ForeignKey("Director",on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Reparto(models.Model):
    character = models.TextField()
    actor = models.ForeignKey("Actor",on_delete=models.CASCADE)
    movie = models.ForeignKey("Peliculas",on_delete=models.CASCADE)
    def __str__(self):
        return self.character