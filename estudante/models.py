from django.db import models

# Create your models here.


class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.nome}'
