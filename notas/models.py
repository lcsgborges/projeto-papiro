from django.db import models
from django.contrib.auth.models import User

class Nota(models.Model):
    titulo = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    conteudo = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.titulo
