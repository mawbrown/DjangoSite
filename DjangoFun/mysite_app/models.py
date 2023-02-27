# Import standard Django Model from built-in library
from django.db import models
from datetime import datetime

# Create your models here.
class MysiteModel(models.Model):

    # Field Names
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    # Image format Year > Month > Date
    image = models.ImageField(upload_to="images/%Y/%m/%d")

    # Rename the instances of the model with their title name
    def __str__(self) -> str:
        return self.title