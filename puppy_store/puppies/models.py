from django.db import models

# Create your models here.

class Puppy(models.Model):
    """
    Puppy Model
    Defines the attributes of a puppy
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_breed(self) -> str:
        return f'{self.name} belongs to {self.breed} breed.'

    def __repr__(self) -> str:
        return f'{self.name} is added.'
