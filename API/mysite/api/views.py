from django.conf import settings
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from .serializers import BirdSerializer, ResultsSerializer, NetworkSerializer, UploadSerializer
from .models import Bird, Results, Networks
from rest_framework.response import Response
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os
from time import sleep
from .predict import UploadedImage


# ModelViewSet will handle GET and POST
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
        file_uploaded = request.FILES['file_uploaded']
        file_type = file_uploaded.content_type
        file_content = ContentFile(file_uploaded.read())
        process_bool = False

        # analyse the data with the AI
        """ My neural network can only accepts keras Image objects, and I cant manage to 
        find a way to convert the file_uploaded into a PIL image. One way to do this is to use a downloaded image and 
        use its path to then make it a keras Image object. """

        if file_type == "image/jpeg":
            print("asdf")
            img = UploadedImage(file_content, "jpg")
            # I would use img.main(), but for some reason it saves the image twice
            img.convert()
        elif file_type == "image/png":
            img = UploadedImage(file_content, "png")
            img.convert()
        else:
            print("unsupported data type")

        # save the result in the result model

        # send a OK response with the results

        response = "POST API and you have uploaded a {} file, the file has been processed".format(file_type) + "  "+str(img.predict())

        return Response(response)


# load_network()
