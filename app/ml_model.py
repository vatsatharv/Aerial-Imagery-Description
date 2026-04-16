import tensorflow as tf
import os

model = None

def get_model():
    global model
    if model is None:
        MODEL_PATH = os.path.join(
            os.path.dirname(__file__),
            "unet_loveda_final.h5"
        )

        model = tf.keras.models.load_model(
            MODEL_PATH,
            compile=False   
        )

        print(" MODEL LOADED SUCCESSFULLY")

    return model