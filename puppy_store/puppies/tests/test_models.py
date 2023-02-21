from django.test import TestCase
from ..models import Puppy

# Create your tests here.

class PuppyTest(TestCase):
    """Test module for puppy model"""

    def setUp(self):
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black'
        )
        Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown'
        )
    
    def test_puppy_breed(self):
        puppy_casper = Puppy.objects.get(name='Casper')
        puppy_muffin = Puppy.objects.get(name='Muffin')
        self.assertEqual(
            puppy_casper.get_breed(), "Casper belongs to Bull Dog breed."
        ) # the returned value has to be equal with the value i set there
        self.assertEqual(
            puppy_muffin.get_breed(), "Muffin belongs to Gradane breed."
        )
