from django.contrib import admin
from interpets2019.models import Petiano

# admin.site.register(Petiano)
@admin.register(Petiano)
class PetianoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pet', 'restricao_alimentar', 'oficina')
    list_filter = ('restricao_alimentar', 'oficina')