from django.db import models
from django.contrib.auth.models import User

TIPOS = [('Vegetariano', 'Vegetariano'), ('Vegano', 'Vegano'), ('Nenhuma', 'Nenhuma')]

class Petiano(models.Model):
    nome = models.CharField(max_length=255, null=False, default='')
    email = models.CharField(max_length=255, unique=True, default='')
    telefone = models.CharField(max_length=255, unique=False,null=True)
    restricao_alimentar = models.CharField(max_length=255, unique=False, default='Nenhuma', choices=TIPOS)
    pet = models.CharField(max_length=25, null=False, default='')
    oficina = models.BooleanField(default=False, null=True)
    credenciado = models.BooleanField(default=False)
    pagou = models.BooleanField(default=False)
    dinamica = models.BooleanField(default=False)

    class Meta:
        ordering = ['pet']

    def __str__(self):
        return str(self.pet) + ' ' + str(self.nome)
