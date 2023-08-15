from rest_framework.viewsets import ModelViewSet

from garagem.models import Modelo
from garagem.serializers import ModeloSerializer

# from rest_framework.permissions import IsAuthenticated


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
