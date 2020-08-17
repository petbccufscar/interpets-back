from rest_framework import serializers
from evento.models import *


class PetianoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Petiano
        #fields = ('nome', 'email', 'telefone', 'restricao_alimentar', 'pet')
        fields = ('nome', 'email', 'telefone', 'pet')

class GDTSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=255)
    quantidade_vagas = serializers.IntegerField()