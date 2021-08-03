import io
import os
import sys
import math
import dlib
import json
import argparse
import cv2 as cv
from math import pi
import pandas as pd
import numpy as np
import skimage.draw
import PySimpleGUI as sg
from fnmatch import fnmatch
from itertools import permutations
from PIL import Image, ImageDraw

def Processing(imagepath):
    # Initialize dlib's shape predictor
    p = "shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(p)
    # Initialize dlib's face detector
    detector = dlib.get_frontal_face_detector()
    # Initialize output
    horizontalCenter = "Horizontally Centered"
    headHeight = "Crown to chin length is appropriate"
    headPose = "Head pose is appropriate"

    # Detecting faces in the grayscale image
    img = cv.imread(imagepath)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    height = np.size(img, 0)
    width = np.size(img, 1)
    
    faces = detector(gray)

    # Get the shape using the predictor
    for face in faces:
        landmarks=predictor(gray, face)
    for n in range(0,68):
        x=landmarks.part(n).x
        y=landmarks.part(n).y
        cv.circle(img, (x, y), 1, (0, 0, 255), -1)

    imgbytes = img


    # Defining x and y coordinates of left and right edge of face
    leftx=landmarks.part(0).x
    rightx=landmarks.part(16).x
    rightside = width - rightx

    # horizontally centered
    if abs(leftx-rightside) < 0.15*max(leftx, rightside):
        pass 
    else:
        horizontalCenter = "not horizontally centered"

    # The distance between the eyebrows and the top of the head is half the distance from the eyebrow to the chin plus allowance for hair
    # Estimate the crown of the head and calculate whether the face (top of head to chin) covers at least 60% of the image

    # Find the maximum point of the eyebrows and y coord of chin
    browpoint = max(landmarks.part(19).y, landmarks.part(24).y)
    chiny = landmarks.part(8).y
    
    browtochin = abs(browpoint -  chiny)
    
    crowntochin = browtochin * 1.75

    facePercent = crowntochin/height

    if facePercent<0.6:
        headHeight = "face is too far away"
    elif facePercent>0.8:
        headHeight = "face is too close"
    else:
        pass

    img = cv.imread(imagepath);
    size = img.shape

    image_points = np.array([
                            (landmarks.part(30).x, landmarks.part(30).y),     # Nose tip
                            (landmarks.part(8).x, landmarks.part(8).y),       # Chin
                            (landmarks.part(36).x, landmarks.part(36).y),     # Left eye left corner
                            (landmarks.part(45).x, landmarks.part(45).y),     # Right eye right corne
                            (landmarks.part(48).x, landmarks.part(48).y),     # Left Mouth corner
                            (landmarks.part(54).x, landmarks.part(54).y)      # Right mouth corner
                        ], dtype="double")

                        
    model_points = np.array([
                            (0.0, 0.0, 0.0),             # Nose tip
                            (0.0, -330.0, -65.0),        # Chin
                            (-165.0, 170.0, -135.0),     # Left eye left corner
                            (165.0, 170.0, -135.0),      # Right eye right corne
                            (-150.0, -150.0, -125.0),    # Left Mouth corner
                            (150.0, -150.0, -125.0)      # Right mouth corner                         
                        ])

    # Camera internals
 
    center = (size[1]/2, size[0]/2)
    focal_length = center[0] / np.tan(60/2 * np.pi / 180)
    camera_matrix = np.array(
                            [[focal_length, 0, center[0]],
                            [0, focal_length, center[1]],
                            [0, 0, 1]], dtype = "double"
                            )

    dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion
    (success, rotation_vector, translation_vector) = cv.solvePnP(model_points, image_points, camera_matrix, dist_coeffs, flags=cv.SOLVEPNP_ITERATIVE)

    
    axis = np.float32([[500,0,0], 
                            [0,500,0], 
                            [0,0,500]])
                              
    imgpts, jac = cv.projectPoints(axis, rotation_vector, translation_vector, camera_matrix, dist_coeffs)
    modelpts, jac2 = cv.projectPoints(model_points, rotation_vector, translation_vector, camera_matrix, dist_coeffs)
    rvec_matrix = cv.Rodrigues(rotation_vector)[0]

    proj_matrix = np.hstack((rvec_matrix, translation_vector))
    eulerAngles = cv.decomposeProjectionMatrix(proj_matrix)[6] 

    
    pitch, yaw, roll = [math.radians(_) for _ in eulerAngles]


    pitch = math.degrees(math.asin(math.sin(pitch)))
    roll = -math.degrees(math.asin(math.sin(roll)))
    yaw = math.degrees(math.asin(math.sin(yaw)))


    if abs(pitch) > 15:
        headPose = "Head is tilted"
    elif abs(roll) > 15:
        headPose = "Head is tilted"
    elif abs(yaw) > 15:
        headPose = "Head is tilted"
    else:
        pass

    return imgbytes, horizontalCenter, headHeight, headPose

