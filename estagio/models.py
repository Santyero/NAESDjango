from django.db import models
from django.contrib.auth.models import User
from estudante.models import Estudante

# Create your models here.
class Estagio(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_termino = models.DateField(null=True, blank=True)
    carga_horaria = models.DecimalField(max_digits=5, decimal_places=2)
    protocolado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    data_protocolo = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.empresa} - {self.estudante}'