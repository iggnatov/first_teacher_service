from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from participants.models import Participant
from participants.serializers import ParticipantSerializer, Participant2Serializer


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


class MakeChoise(UpdateAPIView):

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PATCH not allowed"})

        try:
            instance = Participant.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = Participant2Serializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

