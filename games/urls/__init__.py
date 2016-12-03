from django.conf.urls import url, include

urlpatterns = [
    url(r'^pentago/', include('games.urls.pentago', namespace='pentago')),
]
