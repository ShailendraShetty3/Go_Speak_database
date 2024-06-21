from rest_framework import serializers
from .models import Groups, Cfps, Events, Proposals

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'


class CfpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cfps
        fields = '__all__'


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class ProposalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposals
        fields = '__all__'