from rest_framework import viewsets, status
from rest_framework.response import Response

from interpets2019.models import Petiano
from interpets2019.serializers import PetianoSerializer
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
