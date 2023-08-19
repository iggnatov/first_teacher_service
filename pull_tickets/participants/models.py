from django.db import models

from tickets.models import Tickets


class Participant(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    code_for_link = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=50)
    chosen_ticket_id = models.ForeignKey(Tickets, blank=True, on_delete=models.CASCADE)
    chosen_date = models.DateTimeField(blank=True)
