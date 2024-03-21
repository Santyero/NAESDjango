from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from estudante.models import Estudante
from estudante.serializer import EstudanteSerializer
from rest_framework.serializers import Serializer
# Create your views here.


class EstudanteView(GenericAPIView):
    serializer_class = EstudanteSerializer
    queryset = Estudante.objects.all()
    
    
    def get(request, *args, **kwargs):
        dados = EstudanteSerializer(Estudante.objects.all()).data
        return Response(status=200, data=dados)

    def post(request, *args, **kwargs):
        nome = request.args.get('nome')
        matricula = request.args.get('matricula')
        data_nascimento = request.args.get('data_nascimento')
        email = request.args.get('email')
        
        estudante = Estudante(
            nome,
            matricula,
            data_nascimento,
            email
        )
        estudante.save()
        return Response(status=200, data=estudante)
        

    def delete(request, *args, **kwargs):
        estudante = self.queryset.filter(id=request.args.get('id')).first()
        if not estudante: 
            return Response(status=400)

        estudante.delete()

    def put(request, *args, **kwargs):
        nome = request.args.get('nome')
        matricula = request.args.get('matricula')
        data_nascimento = request.args.get('data_nascimento')
        email = request.args.get('email')
        id = request.param.get('id')
        
        estudante = Estudante.objects.filter(id=id)
        estudante.nome = nome
        estudante.matricula = matricula
        estudante.data_nascimento = data_nascimento
        estudante.email = email
        
        estudante.save()
        
        return Response(status=200, data=estudante)
