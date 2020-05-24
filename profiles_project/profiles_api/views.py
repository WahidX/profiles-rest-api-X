from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):

    def get(self, request, format=None):
        dataList = ['Just','a','sample','list']

        return Response({'message':'Hello X','data':dataList})
        