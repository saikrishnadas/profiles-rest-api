from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our profile object."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'last_login', 'password')
        extra_kwargs = {
            'last_login': {'read_only': True},
            'password': {'write_only': True}
        }

    def create(self,validated_data):
        """creates and returns new users"""
        user = models.UserProfile.create_user(
            email=validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for our profile feed object."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
