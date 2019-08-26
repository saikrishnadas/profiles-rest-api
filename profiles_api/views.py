from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API Views"""
    serializer = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of API Views features"""
        an_apiview=[
            'hey im sai',
            'i am a human',
            'i am a engg too',
            'football fan',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """Creates a hello message with our input name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """put method for update"""
        return Response({"method":"PUT"})


    def patch(self,request,pk=None):
        """patch method for partial update"""
        return Response({"method":"PATCH"})


    def delete(self,request,pk=None):
        """delete a object"""
        return Response({"method":"DELETE"})
