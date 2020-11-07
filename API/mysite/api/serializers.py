from rest_framework import serializers
from .models import Bird, Networks, Results


class BirdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bird
        fields = ('id', 'name')


class ResultsSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:results-detail")

    class Meta:
        model = Results
        fields = ('id', 'url', 'network_id', 'result')


class NetworkSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:networks-detail")

    class Meta:
        model = Networks
        fields = ('id', 'name', 'algorithm')
