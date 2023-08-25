from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from participants.models import Participant
from participants.serializers import ParticipantSerializer
from tickets.models import Ticket


def show_participants(request):
    return render(request, 'participants.html')

"""
API
"""

class ParticipantsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows participants to be viewed or edited.
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
