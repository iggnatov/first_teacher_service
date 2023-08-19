from django.http import HttpResponse


def show_tickets(request):
    return HttpResponse("Tickets")