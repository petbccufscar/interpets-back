from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Petiano(models.Model):
	nome = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	pet_extenso = models.CharField(max_length=100)
	pet_sigla = models.CharField(max_length=25)

	class Meta:
		ordering = ['pet_sigla']

	def __str__(self):
		return str(self.nome) + " " + str(self.pet_sigla)


@receiver(post_save, sender=User)
def create_user_petiano(sender, instance, created, **kwargs):
	if created:
		Petiano.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_petiano(sender, instance, **kwargs):
	instance.petiano.save()
