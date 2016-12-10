from django.contrib.auth.models import User
from rest_framework import serializers

from profiles.models import UserProfile, Team


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'university', 'profile_picture')


class TeamSerializer(serializers.ModelSerializer):
    users = UserProfileSerializer(many=True)

    class Meta:
        model = Team
        fields = ('name', 'users')
