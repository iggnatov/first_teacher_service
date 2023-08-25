from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class ChangeTicket(UpdateAPIView):

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PATCH not allowed"})

        try:
            instance = Ticket.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = TicketSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

