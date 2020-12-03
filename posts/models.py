from django.db import models

# Create your models here.


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
