from rest_framework import serializers

from participants.models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(ParticipantSerializer, self).to_representation(instance)
        try:
            rep['chosen_ticket'] = instance.chosen_ticket.topic
            return rep
        except AttributeError:
            rep['chosen_ticket'] = 'None'
            return rep


class Participant2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
