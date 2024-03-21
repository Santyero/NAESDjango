from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# Create your views here.


class EstagioView(GenericAPIView):
    
    def get(request, *args, **kwargs):
        return Response(status=200, data="aaa")
    
    def post(request, *args, **kwargs):
        return Response(status=200)
    
    def delete(request, *args, **kwargs):
        return Response(status=200)
    
    def put(request, *args, **kwargs):
        return Response(status=200)