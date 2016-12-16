from django.conf.urls import url, include
from rest_framework import routers

from profiles.views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'', ProfileViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
