from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

from garagem.models import Modelo
from garagem.serializers import ModeloSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
