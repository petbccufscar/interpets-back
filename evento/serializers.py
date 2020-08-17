from rest_framework import serializers
from evento.models import Petiano


class PetianoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Petiano
        #fields = ('nome', 'email', 'telefone', 'restricao_alimentar', 'pet')
        fields = ('nome', 'email', 'telefone', 'pet')
