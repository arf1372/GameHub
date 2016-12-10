from django.contrib import admin

from visage.models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'creation_date', 'author')
    search_fields = ('title', 'author__username')
    list_filter = ('state',)
