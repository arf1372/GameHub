from django.db import transaction
from django.contrib.auth.models import User
from rest_framework import serializers

from profiles.models import UserProfile, Team


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(password or user.make_random_password())
        user.save()
        return user

    @transaction.atomic
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super(UserSerializer, self).update(instance, validated_data)
        if password is not None:
            user.set_password(password)
            user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'university', 'profile_picture')

    @transaction.atomic
    def create(self, validated_data):
        validated_data.update({
            'user': UserSerializer().create(validated_data.pop('user', dict()))
        })
        return super(UserProfileSerializer, self).create(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        UserSerializer().update(instance.user, validated_data.pop('user', dict()))
        return super(UserProfileSerializer, self).update(instance, validated_data)


class TeamSerializer(serializers.ModelSerializer):
    users = UserProfileSerializer(many=True)

    class Meta:
        model = Team
        fields = ('name', 'users')
