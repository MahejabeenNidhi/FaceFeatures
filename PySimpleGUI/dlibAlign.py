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

import dlibProcessing

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
            sg.Text("Horizontal Center                                                    ", key="-HOR-"),
        ],
        [
            sg.Text("Head Height                                                          ", key="-HEI-"),
        ],
        [
            sg.Text("Head Pose                                                            ", key="-POS-"),
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
                imgarr, horizontalCenter, headHeight, headPose = dlibProcessing.Processing(filename)
            imgbytes = cv.imencode(".png", imgarr)[1].tobytes()
            window["-IMAGE-"].update(data=imgbytes)
            window["-HOR-"].update(horizontalCenter)
            window["-HEI-"].update(headHeight)
            window["-POS-"].update(headPose)

    window.close()


if __name__ == "__main__":
    main()
