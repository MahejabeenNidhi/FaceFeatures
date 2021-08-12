#!/usr/bin/env python
# coding: utf-8


import asyncio
import io
import glob
import os
import sys
import dlib
import time
import math
import uuid
import requests
from pylab import *
import cv2 as cv
import numpy as np
import pandas as pd
import PySimpleGUI as sg
from itertools import permutations
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from skimage.draw import line, polygon, circle, ellipse



def Glaring(imagepath):
    # Initialize dlib's shape predictor
    p = "shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(p)
    # Initialize dlib's face detector
    detector = dlib.get_frontal_face_detector()
    
    glareState = 'No Glare'
    
    # Load image
    image = cv.imread(imagepath)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    height = np.size(image, 0)
    width = np.size(image, 1)
    
    # Detect image and facial landmarks
    faces = detector(gray)
    for face in faces:
        landmarks=predictor(gray, face)
        
    # Retrieve relevant landmarks
    leftjaw = landmarks.part(3).x
    rightjaw = landmarks.part(13).x
    topbrow = max(landmarks.part(17).y, landmarks.part(18).y, landmarks.part(19).y, landmarks.part(20).y, landmarks.part(21).y, landmarks.part(22).y, landmarks.part(23).y, landmarks.part(24).y, landmarks.part(25).y, landmarks.part(26).y)
    forehead = topbrow * 0.65
    nose = landmarks.part(30).y
    
    # Retrieve left eye landmarks
    point37 = [landmarks.part(36).x, landmarks.part(36).y]
    point38 = [landmarks.part(37).x, landmarks.part(37).y]
    point39 = [landmarks.part(38).x, landmarks.part(38).y]
    point40 = [landmarks.part(39).x, landmarks.part(39).y]
    point41 = [landmarks.part(40).x, landmarks.part(40).y]
    point42 = [landmarks.part(41).x, landmarks.part(41).y]
    
    # Retrieve right eye landmarks
    point43 = [landmarks.part(42).x, landmarks.part(42).y]
    point44 = [landmarks.part(43).x, landmarks.part(43).y]
    point45 = [landmarks.part(44).x, landmarks.part(44).y]
    point46 = [landmarks.part(45).x, landmarks.part(45).y]
    point47 = [landmarks.part(46).x, landmarks.part(46).y]
    point48 = [landmarks.part(47).x, landmarks.part(47).y]
    
    # Fill the right and left eyes
    lefteyepts = np.array((point37, point38, point39, point40, point41, point42), np.int32)
    lefteyepts = lefteyepts.reshape((-1,1,2))
    cv.fillPoly(image, [lefteyepts], (127, 127, 127), 8);
    
    righteyepts = np.array((point43, point44, point45, point46, point47, point48), np.int32)
    righteyepts = righteyepts.reshape((-1,1,2))
    cv.fillPoly(image, [righteyepts], (127, 127, 127), 8);
    
    # Save blocked eyes
    cv.imwrite('blocked.jpg', image)
    
    # Load and crop image to focus on the likely areas of glare
    im = Image.open('blocked.jpg')
    crop_img = im.crop((leftjaw, forehead, rightjaw, nose))
    crop_img.save('cropblock.jpg')
    
    # Convert modified image to YUV colorspace
    img = cv.imread("cropblock.jpg")
    Y = cv.cvtColor(img, cv.COLOR_BGR2YUV)[:,:,0]

    # compute min and max of Y
    mini = max(np.min(Y), 0)
    maxi = np.max(Y)

    # compute contrast
    nume = maxi - mini
    denom = int(maxi) + int(mini)
    contrast = nume/denom
        
    # use HSV
    h, s, v = cv.split(cv.cvtColor(img, cv.COLOR_RGB2HSV))
    intensity = v/255
    saturation = s/255
    
    glarescore = contrast * intensity.max() * (1 - saturation.max())
    
    if intensity.max() >= 1:
        if contrast>0.85:
            glareState = 'Glare Present'
    
    return glareState
    




