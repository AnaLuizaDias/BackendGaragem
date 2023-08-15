from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca
from garagem.serializers import MarcaSerializer

# from rest_framework.permissions import IsAuthenticated


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
