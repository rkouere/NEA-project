from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BirdSerializer, ResultsSerializer, NetworkSerializer
from .models import Bird, Results, Networks

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from drf_multiple_model.views import ObjectMultipleModelAPIView


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


@api_view(['GET', 'POST', 'DELETE'])
def bird_list(request):
    if request.method == "GET":
        birds = Bird.objects.all()

        name = request.query_params.get('name', None)
        if name is not None:
            birds = birds.filter(name_icontains=name)

        birds_serializer = BirdSerializer(birds, many=True)
        return JsonResponse(birds_serializer.data, safe=False)

    elif request.method == "POST":
        bird_data = JSONParser().parse(request)
        bird_serializer = BirdSerializer(data=bird_data)
        if bird_serializer.is_valid():
            bird_serializer.save()
            return JsonResponse(bird_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(bird_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        count = Bird.objects.all().delete()
        return JsonResponse({'message': '{} Birds deleted!'.format(count[0])})


@api_view(['GET', 'PUT', 'DELETE'])
def bird_detail(request, pk):
    try:
        bird = Bird.objects.get(pk=pk)
    except Bird.DoesNotExist:
        return JsonResponse({'message': 'The bird does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = BirdSerializer(bird)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'PUT':
        bird_data = JSONParser().parse(request)
        bird_serializer = BirdSerializer(bird, data=bird_data)
        if bird_serializer.is_valid():
            bird_serializer.save()
            return JsonResponse(bird_serializer.data)
        return JsonResponse(bird.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bird.delete()
        return JsonResponse({'message': 'Birds deleted'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def bird_list_id(request, id):
#     bird = Bird.objects.filter("id" == id)
#
#     if request.method == 'GET':
#         bird_serializer = BirdSerializer(bird, many=False)
#         return JsonResponse(bird_serializer.data, safe=False)


# requests for results database:
@api_view(['GET', 'POST', 'DELETE'])
def results_list(request):
    if request.method == "GET":
        results = Results.objects.all()
        result = request.query_params.get('result', None)
        if result is not None:
            results = results.filter(name_icontains=result)
        results_serializer = ResultsSerializer(results, many=True) # , context={'request': request}
        return JsonResponse(results_serializer.data, safe=False, )

    elif request.method == "POST":
        results_data = JSONParser().parse(request)
        results_serializer = ResultsSerializer(data=results_data)
        if results_serializer.is_valid():
            results_serializer.save()
            return JsonResponse(results_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(results_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        count = Results.objects.all().delete()
        return JsonResponse({'message': '{} Results deleted'.format(count[0])})


@api_view(['GET', 'PUT', 'DELETE'])
def results_detail(request, pk):
    try:
        result = Results.objects.get(pk=pk)
    except Results.DoesNotExist:
        return JsonResponse({'message': 'The result does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = ResultsSerializer(result)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'PUT':
        result_data = JSONParser().parse(request)
        result_serializer = ResultsSerializer(result, data=result_data)
        if result_serializer.is_valid():
            result_serializer.save()
            return JsonResponse(result_serializer.data)
        return JsonResponse(result.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        result.delete()
        return JsonResponse({'message': 'results deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def networks_list(request):
    if request.method == "GET":
        networks = Networks.objects.all()

        name = request.query_params.get('name', None)
        if name is not None:
            networks = networks.filter(name_icontains=name)

        networks_serializer = NetworkSerializer(networks, many=True)
        return JsonResponse(networks_serializer.data, safe=False)

    elif request.method == "POST":
        network_data = JSONParser().parse(request)
        network_serializer = NetworkSerializer(data=network_data)
        if network_serializer.is_valid():
            network_serializer.save()
            return JsonResponse(network_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(network_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        count = Networks.objects.all().delete()
        return JsonResponse({'message': '{} Networks deleted'.format(count[0])})


@api_view(['GET', 'PUT', 'DELETE'])
def networks_detail(request, pk):
    try:
        network = Networks.objects.get(pk=pk)
    except Networks.DoesNotExist:
        return JsonResponse({'message': 'Network not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = NetworkSerializer(network)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'PUT':
        network_data = JSONParser().parse(request)
        network_serializer = NetworkSerializer(network, data=network_data)
        if network_serializer.is_valid():
            network_serializer.save()
            return JsonResponse(network_serializer.data)
        return JsonResponse(network.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        network.delete()
        return JsonResponse({'message': 'Networks deleted'}, status=status.HTTP_204_NO_CONTENT)
