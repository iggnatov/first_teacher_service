from django.shortcuts import render
from rest_framework import viewsets
from tickets.models import Ticket
from tickets.serializers import TicketSerializer


def show_tickets(request):
    return render(request, "tickets.html")


def show_confirmation(request):
    return render(request, 'confirmation.html')


"""
API
"""


class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tickets to be viewed or edited.
    """
    queryset = Ticket.objects.filter(is_available=1)
    serializer_class = TicketSerializer
