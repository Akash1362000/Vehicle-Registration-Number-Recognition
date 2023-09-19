from django.contrib.staticfiles import finders
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import VehicleImage
from .service import process_image


class VehicleImageTestCase(TestCase):
    def setUp(self):
        self.image_path = finders.find("car.jpg")

        with open(self.image_path, "rb") as infile:
            self.test_image = SimpleUploadedFile(self.image_path, infile.read())

    def test_process_image(self):
        result = process_image(image_path=self.image_path)
        self.assertEqual(result.get("registration_number"), "786P0")

    def test_upload_image_view(self):
        response = self.client.post(reverse("upload_image"), {"image": self.test_image})
        self.assertEqual(response.status_code, 302)
        uploaded_image = VehicleImage.objects.first()
        self.test_process_image()

    def test_image_list_view(self):
        response = self.client.get(reverse("image_list"))
        self.assertEqual(response.status_code, 200)
