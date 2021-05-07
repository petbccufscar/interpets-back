from rest_framework import serializers
from evento.models import *

class PetianoSaveSerializer(serializers.ModelSerializer):
    gdt = serializers.PrimaryKeyRelatedField(queryset=GDT.objects.all(), allow_null=True)
    telefone = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Petiano
        fields = ('nome', 'email', 'telefone', 'acessibilidade', 'pet', 'descricao_acessibilidade', 'gdt')

class PetianoCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petiano
        fields = ('nome', 'email', 'telefone', 'acessibilidade', 'pet', 'descricao_acessibilidade', 'gdt')
        depth = 1

class GDTSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = GDT
        fields = ('id', 'nome')

class GDTDescSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = GDT
        fields = ('id', 'nome', 'descricao', 'quantidade_vagas')