from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return HttpResponse("Participants")


class AppRate(APIView):
    @staticmethod
    def get(request):
        # code = self.request.query_params.get('spec_code')
        # mark = self.request.query_params.get('mark')
        # grade = self.request.query_params.get('grade')

        # queryset = Application.objects.filter(spec_c
        response = {}
        return Response(response)