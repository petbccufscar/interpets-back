from rest_framework import viewsets, status
from rest_framework.response import Response

from evento.models import *
from evento.serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class PetianoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Petiano.objects.all()
    serializer_class = PetianoSerializer

    def list(self, request, ** kwargs):
        try:
            queryset = Petiano.objects.get(email=request.query_params['email'])
            serializer = PetianoSerializer(queryset, many=False)
            return Response(serializer.data)
        except:
            return Response({'error': 'usuário não cadastrado'}, status=status.HTTP_404_NOT_FOUND)

class GDTViewSet(viewsets.ModelViewSet):
    def list(self, request, ** kwargs):
        try:
            queryset = GDT.objects.all()
            serializer = GDTDescSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({'error': 'Não há GDTs cadastrados'}, status=status.HTTP_404_NOT_FOUND)

class GDTDisponivelViewSet(viewsets.ModelViewSet):
    def list(self, request, ** kwargs):
        try:
            queryset = GDT.objects.filter(quantidade_vagas__gt=0)
            serializer = GDTSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({'error': 'Não há GDTs disponíveis'}, status=status.HTTP_404_NOT_FOUND)