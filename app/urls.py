from django.conf.urls import url
from rest_framework import routers
from app.views import SongViewSet, CustomView

router = routers.DefaultRouter()
router.register(r'songs', SongViewSet)

urlpatterns = [
    url(r'customview', CustomView.as_view()),
]

urlpatterns += router.urls
