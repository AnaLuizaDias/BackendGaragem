from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

from garagem.models import Veiculo
from garagem.serializers import VeiculoSerializer, VeiculoDetailSerializer, VeiculoListSerializer



class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer