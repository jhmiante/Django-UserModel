from django.db import models

from django.contrib.auth.models import User


#Não é a forma ideal
class Post(models.Model):
    autor = models.CharField(User, verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=100)
    text = models.CharField('Texto', max_length=400)

    def __str__(self):
        return self.titulo
