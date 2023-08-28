from django.urls import path, include, re_path
from rest_framework import routers

from .views import TicketViewSet, show_tickets, show_confirmation, ChangeTicket, CheckTickets, CheckTicketId

router = routers.DefaultRouter()
router.register(r'tickets+', TicketViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    re_path('all+', show_tickets),
    path('confirmation/', show_confirmation),
    path('api/changeticket/<int:pk>/', ChangeTicket.as_view()),
    re_path('api/checktickets+', CheckTickets.as_view()),
    re_path('api/checkticketid+', CheckTicketId.as_view())

]

urlpatterns += router.urls
