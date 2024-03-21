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
        return Response(status=200, data=EstudanteSerializer(queryset, flat=True))

    def post(request, *args, **kwargs):
        return Response(status=200)

    def delete(request, *args, **kwargs):
        return Response(status=200)

    def put(request, *args, **kwargs):
        return Response(status=200)
