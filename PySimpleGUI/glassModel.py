#!/usr/bin/env python
# coding: utf-8

# load and evaluate a saved model
from numpy import loadtxt
from tensorflow.keras.models import load_model

from numpy import asarray
from numpy import save
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from numpy import load 

def glassDetect(imagepath):
    glassStatus = 'No frame across eyes'
    model = load_model('glassesOrNo.h5')

    def load_image(imagepath):
        # load the image
        img = load_img(imagepath, target_size=(200, 200))
        # convert to array
        img = img_to_array(img)
        # reshape into a single sample with 3 channels
        img = img.reshape(1, 200, 200, 3)
        # center pixel data
        img = img.astype('float32')
        img = img - [123.68, 116.779, 103.939]
        return img

    img = load_image(imagepath)

    result = model.predict(img)

    if result[0] == [1.]:
        glassStatus = 'Frames across eyes'
    else:
        pass
        
        
    return glassStatus



