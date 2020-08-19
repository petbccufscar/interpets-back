from rest_framework import serializers
from evento.models import *

class PetianoSaveSerializer(serializers.ModelSerializer):
    gdt = serializers.PrimaryKeyRelatedField(queryset=GDT.objects.all())

    class Meta:
        model = Petiano
        fields = ('nome', 'email', 'telefone', 'pet', 'gdt')

class PetianoCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petiano
        fields = ('nome', 'email', 'telefone', 'pet', 'gdt')
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