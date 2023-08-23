from django.urls import path, re_path, include
from rest_framework import routers

from . import views
from .views import ParticipantsViewSet, show_participants

router = routers.DefaultRouter()
router.register(r'api/participants+', ParticipantsViewSet)

urlpatterns = [
    path('', views.show_participants, name='participants'),
]

urlpatterns += router.urls

urlpatterns = [
    path('', include(router.urls)),
    re_path('all', show_participants)
]

urlpatterns += router.urls
