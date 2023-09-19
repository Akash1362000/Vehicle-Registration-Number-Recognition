from django.shortcuts import redirect, render

from .forms import ImageUploadForm
from .models import VehicleImage
from .service import process_image


def upload_image(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            registration_number = process_image(image.image.path)
            image.registration_number = registration_number
            image.save()
            return redirect("image_list")
    else:
        form = ImageUploadForm()
    return render(request, "upload_image.html", {"form": form})


def image_list(request):
    images = VehicleImage.objects.all()
    return render(request, "image_list.html", {"images": images})
