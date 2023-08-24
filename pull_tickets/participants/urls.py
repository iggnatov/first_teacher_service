from django.urls import path, re_path, include
from rest_framework import routers

from . import views
from .views import ParticipantsViewSet, show_participants, MyViewSet

router = routers.SimpleRouter()
router.register(r'api/participants+', ParticipantsViewSet)
# router.register(r'api/makechoice+', MyViewSet)

urlpatterns = [
    re_path('', include(router.urls)),
    re_path('api/makechoice+', MyViewSet.as_view()),
    re_path('all', show_participants)
]

urlpatterns += router.urls
