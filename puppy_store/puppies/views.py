from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Puppy
from .serializers import PuppySerializer

# Create your views here.

@api_view(['GET', 'PUT', 'DELETE'])
def get_delete_update_puppy(req, pk):
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # get details for a single puppy
    if req.method == 'GET':
        serializer = PuppySerializer(puppy)
        return Response(serializer.data)
    # delete a single puppy
    elif req.method == 'DELETE':
        return Response({})
    # update details of a single puppy
    elif req.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_puppies(req):
    # get all puppies
    if req.method == 'GET':
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data)
    # insert a new record for a puppy
    elif req.method == 'POST':
        return Response({})