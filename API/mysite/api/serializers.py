from rest_framework import serializers
from .models import Bird, Network, Results
from rest_framework.serializers import Serializer, FileField, IntegerField, CharField


# Serializers handle the "translating" of django models (databases) into other formats which we can use
class BirdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bird
        fields = ('id', 'name')


class ResultsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Results
        fields = ('id', 'network_id', 'result')


class NetworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Network
        fields = ('id', 'name')


class UploadSerializer(Serializer):
    # Create all the fields for the uploading of an image
    file_uploaded = CharField()
    result = IntegerField()

    class Meta:
        fields = ['file_uploaded', 'result']
