from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria
from garagem.serializers import CategoriaSerializer

# from rest_framework.permissions import IsAuthenticated


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # permission_classes = [IsAuthenticated]
