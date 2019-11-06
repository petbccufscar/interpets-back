from django.db import models

TIPOS = [('Vegetariano', 'Vegetariano'), ('Vegano', 'Vegano'), ('Nenhuma', 'Nenhuma')]

tipos_gdt = [('Nenhum', 'Nenhum'),
			('Estrutura Horizontal', 'Estrutura Horizontal'),
			('Gestão Interna', 'Gestão Interna'),
			('Desempenho acadêmico', 'Desempenho acadêmico')]

class GDT(models.Model):
	gdt = models.CharField(max_length=255, default='Nenhum', choices=tipos_gdt)
	quantidade_vagas = models.CharField(max_length=1, editable=False)
	petiano = models.ManyToManyField('Petiano', blank=True)
	
	class Meta:
		ordering = ['gdt']

	def __str__(self):
		return str(self.gdt)


class Petiano(models.Model):
	gdt = models.ForeignKey(GDT, blank = True, on_delete=models.CASCADE)

	nome = models.CharField(max_length=255, null=False, default='')
	email = models.CharField(max_length=255, unique=True, default='')
	telefone = models.CharField(max_length=255, unique=False, null=True)
	restricao_alimentar = models.CharField(max_length=255, unique=False, default='Nenhuma', choices=TIPOS)
	pet = models.CharField(max_length=255, null=False, default='')
	credenciado = models.BooleanField(default=False)
	pagou = models.BooleanField(default=False)

	class Meta:
		ordering = ['pet']

	def __str__(self):
		return str(self.pet) + ' ' + str(self.nome)
