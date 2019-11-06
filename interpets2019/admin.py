from django.contrib import admin
from interpets2019.models import Petiano, GDT

admin.site.site_header = 'Interpets 2019'

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


def confirma_e_credencia(modeladmin, request, queryset):
    for petiano in queryset:
        petiano.credenciado = True
        petiano.pagou = True
        petiano.save()

confirma_e_credencia.short_description = 'Confirmar pagamento e credenciar petiano(s)'


@admin.register(GDT)
class GDTAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade_vagas')

@admin.register(Petiano)
class PetianoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pet','gdt','pagou', 'credenciado') #Coloquei o gdt
    list_filter = ('pet', 'pagou', 'credenciado', 'restricao_alimentar')
    search_fields = ['nome']
    actions = [confirma_pagamento, credencia, confirma_e_credencia]
