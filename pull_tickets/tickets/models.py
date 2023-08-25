from django.db import models

from participants.models import Participant


class Ticket(models.Model):
    topic = models.CharField(max_length=255, blank=True)
    is_available = models.SmallIntegerField(default=1, blank=True)
    participant_cfl = models.ForeignKey(
        Participant,
        to_field='code_for_link',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        default=None)

    def __str__(self):
        return f'{self.pk} - {self.topic} - {self.is_available} - {self.participant_cfl}'
