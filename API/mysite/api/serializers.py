from rest_framework import serializers
from .models import Bird, Networks, Results
from rest_framework.serializers import Serializer, FileField


class BirdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bird
        fields = ('id', 'name')


class ResultsSerializer(serializers.HyperlinkedModelSerializer):
    # network_id = serializers.HyperlinkedIdentityField(view_name="api.networks")

    class Meta:
        model = Results
        fields = ('id', 'network_id', 'result')


class NetworkSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:networks-detail")

    class Meta:
        model = Networks
        fields = ('id', 'name', 'algorithm')


class UploadSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']
