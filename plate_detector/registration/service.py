import openalpr


def process_image(image_path) -> dict:
    alpr = openalpr.Alpr(
        "us",
        "/etc/openalpr/openalpr.conf",
        "/usr/share/openalpr/runtime_data",
    )
    results = alpr.recognize_file(image_path)
    if results["results"]:
        return {
            "registration_number": results.get("results")[0].get("plate"),
            "accuracy": round(results.get("results")[0].get("confidence"), 2),
        }
    else:
        return {
            "registration_number": "None",
            "accuracy": 0.0,
        }
