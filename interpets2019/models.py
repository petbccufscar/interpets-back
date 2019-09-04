from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

TIPOS = [('Vegetariano', 'Vegetariano'), ('Vegano', 'Vegano'), ('Nenhuma', 'Nenhuma')]

class Oficina(models.Model):
    nome = models.CharField(max_length=255, null=False, default='')
    qtde_vagas = models.IntegerField(null = True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return str(self.nome)

class GDT(models.Model):
    nome = models.CharField(max_length=255, null=False, default='')
    qtde_vagas = models.IntegerField(null = True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return str(self.nome)

class Petiano(models.Model):
    nome = models.CharField(max_length=255, null=False, default='')
    email = models.CharField(max_length=255, unique=True, default='')
    telefone = models.CharField(max_length=255, unique=False,null=True)
    restricao_alimentar = models.CharField(max_length=255, unique=False, default='Nenhuma', choices=TIPOS)
    pet = models.CharField(max_length=25, null=False, default='')
    gdt_pk = models.ForeignKey(GDT, null = True, on_delete=models.SET_NULL)
    credenciado = models.BooleanField(default=False)
    pagou = models.BooleanField(default=False)
    oficina_pk = models.ForeignKey(Oficina, null = True, on_delete=models.SET_NULL)
    grupo_dinamica = models.IntegerField(null = True, default = 0)
    class Meta:
        ordering = ['pet']

    def __str__(self):
        return str(self.pet) + ' ' + str(self.nome)

    def save(self, *args, **kwargs):
        try:
            if self.gdt_pk.qtde_vagas > 0:
                self.gdt_pk.qtde_vagas -= 1
                self.gdt_pk.save()
        except:
            pass
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def clean(self):
        if self.oficina_pk.qtde_vagas == 0:
            raise ValidationError("GDT Cheio, favor escolher outro!!!!")
