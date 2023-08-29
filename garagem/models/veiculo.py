from django.db import models

from garagem.models import Acessorio, Cor, Modelo
from uploader.models import Image


class Veiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    capa = models.ManyToManyField(
        Image,
        related_name="+",
    )

    def __str__(self):
        return f"{self.modelo} ({self.ano}), {self.cor}"
