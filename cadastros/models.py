from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.nome}/{self.estado}"
    
    class Meta:
        ordering = ["nome", "estado"]

    