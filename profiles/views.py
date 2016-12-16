from django.db import transaction
from rest_framework import viewsets
from rest_framework_jwt import authentication

from profiles import permissions, serializers
from profiles.models import UserProfile


class ProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.JSONWebTokenAuthentication]
    permission_classes = [permissions.IsCreationOrIsRetrievalOrIsAuthenticated]
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

    @transaction.atomic
    def perform_destroy(self, instance):
        instance.user.delete()
