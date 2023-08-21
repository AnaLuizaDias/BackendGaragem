from django.db import models


class Acessorio(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} ({self.id})"
