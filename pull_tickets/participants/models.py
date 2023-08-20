from django.db import models
from tickets.models import Ticket


class Participant(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    code_for_link = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=50)
    chosen_ticket = models.ForeignKey(Ticket, null=True, blank=True, on_delete=models.CASCADE)
    chosen_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name[:1]} - {self.code_for_link} - {self.chosen_ticket}'
