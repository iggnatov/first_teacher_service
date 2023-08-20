from rest_framework import serializers
from tickets.views import Ticket


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['topic', 'is_available']
