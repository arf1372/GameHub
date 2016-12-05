from django.contrib.auth.models import User
from rest_framework import serializers

from profiles.models import UserProfile, Team, UserTeam


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(username=validated_data.get('email'), **validated_data)
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'university', 'profile_picture')

    def create(self, validated_data):
        university = validated_data.pop('university')
        profile_picture = validated_data.pop('profile_picture')
        user = UserSerializer.create(**validated_data)

        user_profile = UserProfile.objects.create(user=user, university=university, profile_picture=profile_picture)
        return user_profile


class TeamSerializer(serializers.ModelSerializer):
    users = UserProfileSerializer(many=True)

    class Meta:
        model = Team
        fields = ('name', 'users')

    def create(self, validated_data):
        name = validated_data.pop('name')
        users_data = validated_data.pop('users')

        team = Team.objects.create(name=name)
        for user_data in users_data:
            user = UserSerializer.create(**user_data)
            UserTeam.objects.create(user=user, team=team)

        return team
