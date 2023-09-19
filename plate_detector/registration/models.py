from django.db import models


class VehicleImage(models.Model):
    image = models.ImageField(upload_to="uploads")
    registration_number = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return self.image.name
