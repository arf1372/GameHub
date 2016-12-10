from django.contrib import admin

from visage.models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'creation_date', 'expire_date')
    search_fields = ('title',)
    list_filter = ('state',)
