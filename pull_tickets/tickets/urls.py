from django.urls import path, re_path

# from . import views
from .views import TicketList

urlpatterns = [
    re_path('api/tickets+', TicketList.as_view()),
    # path('', views.show_tickets, name='tickets'),
]