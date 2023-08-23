from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from participants.models import Participant
from participants.serializers import ParticipantSerializer
from tickets.models import Ticket
from tickets.serializers import TicketSerializer


def show_participants(request):
    return render(request, 'participants.html')


class ParticipantsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows participants to be viewed or edited.
    """
    queryset = Participant.objects.exclude(chosen_ticket=None)
    serializer_class = ParticipantSerializer
    queryset2 = Ticket.objects.filter(is_available=0)
    serializer_class2 = TicketSerializer
