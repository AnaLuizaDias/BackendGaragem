from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

from garagem.models import Marca
from garagem.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
