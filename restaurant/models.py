import uuid

from django.db import models


# Create your models here.

class Restaurant(models.Model):
    restaurant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    tags = models.JSONField(default=list)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name