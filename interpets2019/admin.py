from django.contrib import admin
from interpets2019.models import Petiano, Oficina
from random import randint

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

def sorteia_dinamicas(modeladmin, request, queryset):
    for petiano in queryset:
        petiano.grupo_dinamica = randint(1, 8)
        petiano.save()
sorteia_dinamicas.short_description = 'Sortear grupos de dinâmica'

def reset_dinamicas(modeladmin, request, queryset):
    for petiano in queryset:
        petiano.grupo_dinamica = 0
        petiano.save()
reset_dinamicas.short_description = 'Resetar grupos de dinâmica'

# admin.site.register(Petiano)
@admin.register(Petiano)
class PetianoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pet', 'pagou', 'credenciado', 'oficina', 'grupo_dinamica')
    list_filter = ('pet', 'oficina', 'pagou', 'dinamica','credenciado', 'grupo_dinamica', 'restricao_alimentar')
    search_fields = ['nome']
    actions = [confirma_pagamento, credencia, sorteia_dinamicas, reset_dinamicas]

@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'qtde_vagas')