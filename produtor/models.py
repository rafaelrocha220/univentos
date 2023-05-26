from django.db import models


class Produtor(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Eventos(models.Model):
    nome = models.CharField(max_length=100)
    tipo_evento = models.CharField(max_length=100)

    data_inicio = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    qtd_ingresso = models.CharField(max_length=100)
    valor_ingresso = models.CharField(max_length=100)
    taxa_univentos = models.BooleanField(default=False)

    imagem = models.ImageField(upload_to='static/', blank=True, null=True)
