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

import glassModel

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
        ],
        [
            sg.Text("Frame across eyes                                                    ", key="-FRA-"),
        ],
    ]

    window = sg.Window("Image Viewer", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                imgarr = cv.imread(filename)
                prediction = glassModel.glassDetect(filename)
            imgbytes = cv.imencode(".png", imgarr)[1].tobytes()
            window["-IMAGE-"].update(data=imgbytes)
            window["-FRA-"].update(prediction)

    window.close()


if __name__ == "__main__":
    main()
