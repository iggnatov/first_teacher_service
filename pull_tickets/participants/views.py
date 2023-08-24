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



class ParticipantsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows participants to be viewed or edited.
    """
    queryset = Participant.objects.exclude(chosen_ticket=None)
    serializer_class = ParticipantSerializer


class MyViewSet(APIView):
    def get(self, request):
        cfl = self.request.query_params.get('cfl')
        tid = self.request.query_params.get('tid')

        participant = Participant.objects.filter(code_for_link=cfl)
        participant.chosen_ticket = tid

        ticket = Ticket.objects.filter(pk=tid)
        ticket.is_available = 0

        response = {
            'y': len(participant),
            'cfl': cfl,
            'tid': tid
        }
        return Response(response, status=status.HTTP_200_OK)
