from django.urls import path, re_path, include
from rest_framework import routers

from .views import ParticipantsViewSet, show_participants, MakeChoise

router = routers.DefaultRouter()
router.register(r'participants+', ParticipantsViewSet)
# router.register(r'makechoise+', MakeChoise)

urlpatterns = [
    path('api/', include(router.urls)),
    re_path('all+', show_participants),
    path('api/plist/', MakeChoise.as_view()),
    path('api/plist/<int:pk>/', MakeChoise.as_view())
]

urlpatterns += router.urls


