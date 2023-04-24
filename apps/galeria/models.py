from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

OPCOES_CATEGORIA = [
    ("NEBULOSA", "Nebulosa"),
    ("ESTRELA", "Estrela"),
    ("GALÁXIA", "Galáxia"),
    ("PLANETA", "Planeta")
]

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    publicada = models.BooleanField(default=True)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    data_fotografia = models.DateField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(    
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.nome
