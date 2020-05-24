from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        dataList = ['Just','a','sample','list']

        return Response({'message':'Hello X','data':dataList})

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
    
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pl=None):
        return Response({'method': 'put'})

    def patch(self, request, pl=None):
        return Response({'method': 'patch'})


    def delete(self, request, pl=None):
        return Response({'method': 'delete'})