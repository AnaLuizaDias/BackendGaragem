     

from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import MarcaViewSet, CategoriaViewSet, CorViewSet, AcessorioViewSet, ModeloViewSet

router = DefaultRouter()
router.register(r"Marcas", MarcaViewSet)
router.register(r"Categoria", CategoriaViewSet)
router.register(r"Cor", CorViewSet)
router.register(r"Acessorio", AcessorioViewSet)
router.register(r"Modelo", ModeloViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
