from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from participants.models import Participant
from participants.serializers import ParticipantSerializer


def show_participants(request):

    return render(request, 'participants.html')



class ParticipantsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows participants to be viewed or edited.
    """
    queryset = Participant.objects.exclude(chosen_ticket=None)
    serializer_class = ParticipantSerializer


class MyViewSet(APIView):
    # queryset = Participant.objects.filter(chosen_ticket=None)
    # serializer_class = ParticipantSerializer

    def get_object(self, code_for_link):
        print(code_for_link)
        try:
            return Participant.objects.get(code_for_link=code_for_link)
        except Participant.DoesNotExist:
            raise Http404

    def get(self, request, code_for_link, format=None):
        participant = self.get_object(code_for_link)
        print(participant)
        # serializer = ParticipantSerializer(participant)
        # return Response(serializer.data)
        serializer = ParticipantSerializer(participant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, code_for_link, format=None):
        participant = self.get_object(code_for_link)
        print(participant)
        serializer = ParticipantSerializer(participant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)