from rest_framework import serializers

from visage.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Announcement
        fields = ('title', 'text', 'creation_date', 'author')
