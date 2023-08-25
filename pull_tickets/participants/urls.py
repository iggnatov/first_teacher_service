from django.urls import path, re_path, include
from rest_framework import routers

from .views import ParticipantsViewSet, show_participants

router = routers.DefaultRouter()
router.register(r'participants+', ParticipantsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    re_path('all+', show_participants)
]

urlpatterns += router.urls


