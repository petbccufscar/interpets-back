from django.contrib import admin
from interpets2019.models import Petiano


def confirma_pagamento(modeladmin, request, queryset):
	for petiano in queryset:
		petiano.pagou = True
		petiano.save()


confirma_pagamento.short_description = 'Confirma Pagamento'


def credencia(modeladmin, request, queryset):
	for petiano in queryset:
		petiano.credenciado = True
		petiano.save()


credencia.short_description = 'Credenciar petiano(s)'


@admin.register(Petiano)
class PetianoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'pet', 'pagou', 'credenciado')
	list_filter = ('pet', 'pagou', 'credenciado', 'restricao_alimentar')
	search_fields = ['nome']
	actions = [confirma_pagamento, credencia]
