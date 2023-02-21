import json
from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from ..models import Puppy
from ..serializers import PuppySerializer

# initialize the APIClient app
client = Client()