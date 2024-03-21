from rest_framework import serializers
from estudante.models import Estudante

class EstudanteSerializer(serializers.SerializerMetaclass):
    
    def Meta():
        model: Estudante
        fields: [
            'nome',
            'matricula',
            'data_nascimento',
            'email'
        ]