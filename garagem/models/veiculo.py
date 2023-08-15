from django.db import models

from garagem.models import Acessorio, Categoria, Cor, Marca, Modelo
from uploader.models import Image


class Veiculo(models.Model):
    descricao = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}), {self.cor}"
