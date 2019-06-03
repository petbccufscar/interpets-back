from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from interpets2019.models import Petiano
from interpets2019.serializers import PetianoSerializer, UserSerializer, GroupSerializer


class PetianoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Petiano.objects.all()
    serializer_class = PetianoSerializer

    def list(self, request, ** kwargs):
        try:
            queryset = Petiano.objects.get(email=request.query_params['email'])
            serializer = PetianoSerializer(queryset, many=False)
            return Response(serializer.data)
        except:
            return Response({'error': 'usuário não cadastrado'}, status=status.HTTP_404_NOT_FOUND)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
