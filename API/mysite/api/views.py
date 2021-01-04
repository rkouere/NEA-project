from django.conf import settings
from django.http import JsonResponse
from django.views.generic import DetailView
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet
from .serializers import BirdSerializer, ResultsSerializer, NetworkSerializer, UploadSerializer
from .models import Bird, Results, Network
from rest_framework.response import Response
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os
from time import sleep
from .predict import UploadedImage
from .database_requests import get_accuracy_rate, rosa_add_result, vgg_add_result



# ModelViewSet will handle GET and POST
class BirdViewSet(viewsets.ModelViewSet):
    queryset = Bird.objects.all()
    serializer_class = BirdSerializer


class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all().order_by('result')
    serializer_class = ResultsSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all().order_by('name')
    serializer_class = NetworkSerializer


# Handles the uploading of images and data
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        string_uploaded = request.POST['file_uploaded']
        result = request.POST['result']

        if int(result) == 0:
            result = False
        elif int(result) == 1:
            result = True
        else:
            result = None
        # file_type = file_uploaded.content_type
        # file_content = ContentFile(file_uploaded.read())

        """ My neural network can only accepts keras Image objects, and I cant manage to 
        find a way to convert the file_uploaded into a PIL image. One way to do this is to use a downloaded image and 
        use its path to then make it a keras Image object. """

        # Makes sure the code doesn't break if a file type it cannot process gets processed
        # if file_type == "image/jpeg":
        #     img = UploadedImage(file_content, "jpg")
        #     img.convert()
        #     process_bool = True
        # elif file_type == "image/png":
        #     img = UploadedImage(file_content, "png")
        #     img.convert()
        #     process_bool = True
        # else:
        #     print("unsupported data type", file_type)
        #     process_bool = False

        img = UploadedImage(string_uploaded)
        img.convert()

        # Only carries on if the file type is correct
        rosa_prediction, vgg_prediction = img.predict()
        res = True
        try:
            bird = Bird.objects.get(name=vgg_prediction)
        except Bird.DoesNotExist:
            res = False
        response = str(rosa_prediction) + ", " + str(res)

        if rosa_prediction == result:
            rosa_add_result(1)
        else:
            rosa_add_result(0)

        if vgg_prediction == result:
            vgg_add_result(1)
        else:
            vgg_add_result(0)
        # print(Response(response))
        # print(string_uploaded, result)
        return Response(response)


# Returns the accuracy rate
class GetAccuracyRate(ViewSet):

    def list(self, request):
        response = get_accuracy_rate('{}ROSA6{}') + get_accuracy_rate('{}VGG-16{}')
        return Response(response)
