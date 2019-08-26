from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API Views"""

    def get(self,request,format=None):
        """Returns a list of API Views features"""
        an_apiview=[
            'hey im sai',
            'i am a human',
            'i am a engg too',
            'football fan',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
