from django.urls import path, include, re_path
from rest_framework import routers
from .views import TicketViewSet, show_tickets

router = routers.DefaultRouter()
router.register(r'api/tickets+', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path('all', show_tickets)
]

urlpatterns += router.urls
