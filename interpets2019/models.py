from django.db import models
from django.contrib.auth.models import User


class Petiano(models.Model):
	nome = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, unique=True)
	pet_extenso = models.CharField(max_length=100, null=False)
	pet_sigla = models.CharField(max_length=25, null=False)

	class Meta:
		ordering = ['pet_sigla']

	def __str__(self):
		return str(self.nome) + " " + str(self.pet_sigla)
