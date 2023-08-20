from django.db import models


class Ticket(models.Model):
    topic = models.CharField(max_length=255)
    is_available = models.SmallIntegerField(default=1)

    def __str__(self):
        return f'{self.pk} - {self.topic} - {self.is_available}'
