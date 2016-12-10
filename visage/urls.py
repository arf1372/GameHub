from django.conf.urls import url

from visage.views import ListAnnouncements


urlpatterns = [
    url(r'^announcements/', ListAnnouncements.as_view(), name='announcements')
]
