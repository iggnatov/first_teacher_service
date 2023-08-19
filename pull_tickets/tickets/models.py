from django.db import models


class Tickets(models.Model):
    topic = models.CharField(max_length=255)
    is_available = models.SmallIntegerField(default=0)
