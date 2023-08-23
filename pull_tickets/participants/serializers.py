from rest_framework import serializers

from participants.models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(ParticipantSerializer, self).to_representation(instance)
        rep['chosen_ticket'] = instance.chosen_ticket.topic
        return rep

        # fields = ['id', 'first_name', 'last_name', 'code_for_link', 'email', 'chosen_ticket', 'chosen_date']