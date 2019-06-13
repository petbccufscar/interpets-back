from django.contrib import admin
from interpets2019.models import Petiano

def confirma_pagamento(modeladmin, request, queryset):
    for petiano in queryset:
        petiano.pagou = True
        petiano.save()
confirma_pagamento.short_description = 'Confirma Pagamento'

# admin.site.register(Petiano)
@admin.register(Petiano)
class PetianoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pet', 'restricao_alimentar', 'oficina', 'pagou', 'credenciado')
    list_filter = ('restricao_alimentar', 'oficina', 'pet', 'pagou', 'credenciado')
    actions = [confirma_pagamento, ]