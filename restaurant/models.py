import uuid

from django.db import models


# Create your models here.

class Restaurant(models.Model):
    restaurant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    place_id =  models.CharField(max_length=100, unique=True, editable=True, null=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    tags = models.JSONField(default=list)
    upload_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name