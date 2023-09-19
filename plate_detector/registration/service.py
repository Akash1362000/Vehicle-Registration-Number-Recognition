import openalpr


def process_image(image_path) -> str:
    alpr = openalpr.Alpr(
        "us",
        "/etc/openalpr/openalpr.conf",
        "/usr/share/openalpr/runtime_data",
    )
    results = alpr.recognize_file(image_path)
    if results["results"]:
        return results["results"][0]["plate"]
    else:
        return "None"
