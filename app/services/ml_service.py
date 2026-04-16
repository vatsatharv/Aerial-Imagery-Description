import numpy as np
from PIL import Image
from app.ml_model import get_model

# Class labels (adjust if needed)
CLASSES = ["Urban", "Rural", "Water", "Vegetation"]

def preprocess_image(file_path):
    image = Image.open(file_path).convert("RGB")
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def generate_description(file_path):
    try:
        model = get_model()

        img = preprocess_image(file_path)

        preds = model.predict(img)[0]  # (256, 256, num_classes)

        # Convert to class map
        class_map = np.argmax(preds, axis=-1)

        # Count pixels per class
        unique, counts = np.unique(class_map, return_counts=True)
        total_pixels = class_map.size

        class_percentages = {
            CLASSES[int(u)]: round((c / total_pixels) * 100, 2)
            for u, c in zip(unique, counts)
        }

        # Sort by dominance
        sorted_classes = sorted(
            class_percentages.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # Build description
        dominant_class, dominant_percent = sorted_classes[0]

        description = f"The aerial image is predominantly {dominant_class} ({dominant_percent}%)."

        if len(sorted_classes) > 1:
            secondary_class, secondary_percent = sorted_classes[1]
            description += f" It also contains {secondary_class} ({secondary_percent}%)."

        return description

    except Exception as e:
        return f"Error in ML processing: {str(e)}"