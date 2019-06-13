from django.contrib import admin
from interpets2019.models import Petiano, Oficina

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

# admin.site.register(Petiano)
@admin.register(Petiano)
class PetianoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pet', 'pagou', 'credenciado', 'oficina', 'dinamica')
    list_filter = ('pet', 'oficina', 'pagou', 'dinamica','credenciado', 'restricao_alimentar')
    search_fields = ['nome']
    actions = [confirma_pagamento, credencia]

@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'qtde_vagas')