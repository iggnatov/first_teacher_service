from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from tickets.models import Ticket


def show_tickets(request):
    return HttpResponse("Tickets")


class TicketList(APIView):
    def get(self, request):
        code = self.request.query_params.get('code')
        topic = self.request.query_params.get('topic')

        queryset = Ticket.objects.filter(is_available=1)

        id_list = []
        id_list_query = queryset.values_list('id', flat=True)
        for elem in id_list_query:
            id_list.append(str(elem))

        if topic == '0':
            response = {}

            for i in range(len(queryset)):
                if queryset[i].is_available == 1:
                    response[queryset[i].id] = queryset[i].topic
                else:
                    continue

            return Response(response)

        elif topic in id_list:
            if queryset[int(topic)-1].is_available == 1:
                response = {
                    "topic_": queryset[int(topic)-1].topic,
                    "code": code,
                    "topic": topic
                }

                return Response(response)
            else:
                return Response('Error')

        else:
            return Response(id_list)
