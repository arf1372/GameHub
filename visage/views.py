from rest_framework import permissions
from rest_framework.generics import ListAPIView

from visage.models import Announcement
from visage.serializers import AnnouncementSerializer


class ListAnnouncements(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Announcement.objects.filter(state='A').order_by('-creation_date')
    serializer_class = AnnouncementSerializer

