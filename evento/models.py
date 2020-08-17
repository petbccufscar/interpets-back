from django.db import models

TIPOS = [('Vegetariano', 'Vegetariano'),
         ('Vegano', 'Vegano'), ('Nenhuma', 'Nenhuma')]

"""
tipos_gdt = [('Nenhum', 'Nenhum'),
			('Estrutura Horizontal', 'Estrutura Horizontal'),
			('Gestão Interna', 'Gestão Interna'),
			('Desempenho acadêmico', 'Desempenho acadêmico')]
"""


class GDT(models.Model):
    nome = models.CharField(max_length=255, default='', null=True, blank=False)
    quantidade_vagas = models.IntegerField(null=True, blank=False)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return str(self.nome)


class Petiano(models.Model):
    gdt = models.ForeignKey(
        GDT,
        blank=True,
        on_delete=models.CASCADE,
        related_name='gdt_do_petiano',
        null=True)
    nome = models.CharField(max_length=255, null=False, default='')
    email = models.CharField(max_length=255, unique=True, default='')
    telefone = models.CharField(max_length=255, unique=False, null=True)
    '''restricao_alimentar = models.CharField(
        max_length=255,
        unique=False,
        default='Nenhuma',
        null=True,
        choices=TIPOS)'''
    pet = models.CharField(max_length=255, null=False, default='')
    credenciado = models.BooleanField(default=False)
    #pagou = models.BooleanField(default=False)

    class Meta:
        ordering = ['pet']

    def __str__(self):
        return str(self.pet) + ' ' + str(self.nome)

    def save(self, *args, **kwargs):
        try:
            if self.gdt.quantidade_vagas > 0:
                self.gdt.quantidade_vagas -= 1
                self.gdt.save()
        except BaseException:
            pass
        super().save(*args, **kwargs)
