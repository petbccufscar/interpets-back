from django.contrib.auth.models import User, Group
from rest_framework import serializers
from interpets2019.models import Petiano


class PetianoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Petiano
        fields = ('nome', 'email', 'pet_sigla', 'pet_extenso')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
