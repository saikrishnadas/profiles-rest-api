from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import ISAUTHENTICATED

from profiles_api import serializers
from profiles_api import permissions
from profiles_api import models

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


class HelloViewSet(viewsets.ViewSet):
    """Test viewset api"""
    serializer = serializers.HelloSerializer

    def list(self,request):
        """returns the list"""

        a_viewset = [
            'Hey!This is viewset',
            'This is the 2nd unit of the course',
            'This is viewset ',
            'needs only less code',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        """Returns Hello user"""
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello user {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self,request,pk=None):
        """updates an object"""
        return Response({'message':'GET'})

    def update(self,request,pk=None):
        """updates an object"""
        return Response({'message':'POST'})

    def partial_update(self,request,pk=None):
        """updates an object"""
        return Response({'message':'PATCH'})

    def destroy(self,request,pk=None):
        """updates an object"""
        return Response({'message':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles create and updating user profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Create token for user login"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    """Handles create and updating user feeds """
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (
        permissions.UpdateOwnStatus,
        ISAUTHENTICATED,
    )

    def perform_create(self,serializer):
        """Sets the user profile to logged in user"""
        serializer.save(user_profile=self.request.user)
