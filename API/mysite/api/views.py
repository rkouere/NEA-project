from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from .serializers import BirdSerializer, ResultsSerializer, NetworkSerializer, UploadSerializer
from .models import Bird, Results, Networks
from rest_framework.response import Response


# # ModelViewSet will handle GET and POST
class BirdViewSet(viewsets.ModelViewSet):
    queryset = Bird.objects.all().order_by('name')
    serializer_class = BirdSerializer


class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all().order_by('result')
    serializer_class = ResultsSerializer


class NetworksViewSet(viewsets.ModelViewSet):
    queryset = Networks.objects.all().order_by('name')
    serializer_class = NetworkSerializer

'''
    Class to upload an image.
'''
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        # analyse the data with the AI

        # save the result in the result model

        # send a OK response with the results
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)
