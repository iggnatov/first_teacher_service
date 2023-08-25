from django.db import models


class Participant(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    code_for_link = models.CharField(max_length=10, blank=True, unique=True)
    email = models.EmailField(max_length=50, blank=True)
    # chosen_ticket = models.ForeignKey(Ticket, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name[:1]} - {self.code_for_link}'
