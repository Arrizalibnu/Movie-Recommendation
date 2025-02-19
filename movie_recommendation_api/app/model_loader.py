import tensorflow as tf

def load_model():
    model_path = "models/recommendation_movie_model_ncf.h5"
    model = tf.keras.models.load_model(model_path)
    return model