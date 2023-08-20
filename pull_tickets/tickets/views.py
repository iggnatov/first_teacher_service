from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from tickets.models import Ticket


def show_tickets(request):
    return HttpResponse("Tickets")


class TicketList(APIView):
    def get(self, request):
        code = self.request.query_params.get('code')

        queryset = Ticket.objects.filter(is_available=0)
        response = {}

        for i in range(len(queryset)):
            if queryset[i].is_available == 0:
                response[queryset[i].id] = queryset[i].topic
            else:
                continue

        return Response(response)