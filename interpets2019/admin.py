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


def confirma_e_credencia(modeladmin, request, queryset):
    for petiano in queryset:
        petiano.credenciado = True
        petiano.pagou = True
        petiano.save()

confirma_e_credencia.short_description = 'Confirmar pagamento e credenciar petiano(s)'


def define_gdt(modeladmin, request, queryset):
    for petiano in queryset:
        petiano.gdt = tipos_gdt #Precisaria passar o gdt q ta la em tipos_gdt como parametro, mas como ?
        petiano.save()

define_gdt.short_description = 'Define GDT'


# Não sei se ta certo :(
#
#@admin.register(GDT)
#class GDTAdmin(admin.ModelAdmin):
#    list_display = ('gdt', 'quantidade_vagas')
#    list_filter = ('gdt')
#    search_fields = ['gdt']
#    actions = [define_gdt]
#


@admin.register(Petiano)
class PetianoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pet', 'gdt', 'pagou', 'credenciado') #Coloquei o gdt
    list_filter = ('pet', 'pagou', 'credenciado', 'restricao_alimentar')
    search_fields = ['nome']
    actions = [confirma_pagamento, credencia, confirma_e_credencia, define_gdt]
