import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
%matplotlib inline

img_path = 'dog.png'
img_path2 = 'dog2.jpg'
img_path3 = 'dog3.jpg'
img_path4 = 'dog4.jpg'
img_path5 = 'animal1.jpg'
img_path6 = 'animal2.jpg


# Import image and preprocess_input
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, ResNet50, decode_predictions

# Load the image with the right target size for your model
img = image.load_img(img_path6, target_size=(224, 224))

# Turn it into an array
img_array = image.img_to_array(img)

# Expand the dimensions of the image, this is so that it fits the expected model input format
img_expanded = np.expand_dims(img_array, axis = 0)

# Pre-process the img in the same way original images were
img_ready = preprocess_input(img_expanded)

model = ResNet50(weights='imagenet')

# Predict with ResNet50 on your already processed img
preds = model.predict(img_ready)

# Decode the first 3 predictions
print('Predicted:', decode_predictions(preds, top=3)[0])

plt.imshow(img)
