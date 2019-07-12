from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField()
    senha = models.CharField()

    # Usar JWT...
