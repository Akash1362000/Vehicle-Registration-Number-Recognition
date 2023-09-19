from django import forms

from .models import VehicleImage


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = VehicleImage
        fields = ["image"]
