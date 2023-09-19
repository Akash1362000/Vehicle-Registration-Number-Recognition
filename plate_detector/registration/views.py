from django.db.models import Max
from django.shortcuts import redirect, render

from .forms import ImageUploadForm
from .models import VehicleImage
from .service import process_image


def upload_image(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            processed_data = process_image(image.image.path)
            image.registration_number = processed_data.get("registration_number")
            image.accuracy = processed_data.get("accuracy")
            image.save()
            return redirect("image_list")
    else:
        form = ImageUploadForm()
    return render(request, "upload_image.html", {"form": form})


def image_list(request):
    images = VehicleImage.objects.all().filter().order_by("-modified")
    max_accuracy = images.aggregate(Max("accuracy")).get("accuracy__max") or 0.0
    return render(
        request,
        "image_list.html",
        {
            "images": images,
            "total_vehicles": images.count(),
            "max_accuracy": max_accuracy,
        },
    )
