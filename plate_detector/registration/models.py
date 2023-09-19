from django.db import models
from django_extensions.db.models import TimeStampedModel


class VehicleImage(TimeStampedModel):
    image = models.ImageField(upload_to="uploads")
    registration_number = models.CharField(max_length=20, blank=True)
    accuracy = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.image.name[8:]
