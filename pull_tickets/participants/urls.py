from django.urls import path, re_path, include
from rest_framework import routers

from . import views
from .views import ParticipantsViewSet, show_participants, MyViewSet

router = routers.SimpleRouter()
router.register(r'api/participants+', ParticipantsViewSet)
# router.register(r'api/makechoice/<int:code_for_link>', MyViewSet)

urlpatterns = [
    # path('', views.show_participants, name='participants'),
    path('api/makechoice/<int:code_for_link>', MyViewSet.as_view()),
    re_path('all', show_participants)
]

urlpatterns += router.urls
