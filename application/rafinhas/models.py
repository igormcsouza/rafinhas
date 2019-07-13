from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=10)
    senha = models.CharField(max_length=20)

    # Usar JWT...
