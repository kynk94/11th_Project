# Face landmarks Detection
# usage:
# python facial_landmark_detection.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/face1.jpg

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import os
import imutils
import dlib
import cv2
import matplotlib.pyplot as plt

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

if os.path.isfile(args["shape_predictor"]):
	pass
else:
	# print("Oops...! File is not available. Shall I downlaod ?")
	cmd = "wget -c --progress=bar http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"
	os.system(cmd)

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# load the input image, resize it, and convert it to grayscale
image = dlib.load_rgb_image(args["image"]) 
orig = image
image = imutils.resize(image, width=512)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
#rects = detector(gray, 1)
rects = detector(image, 1)

import numpy as np
images = np.ones_like(image)*255 #white background


# loop over the face detections
for (i, rect) in enumerate(rects):
	# determine the facial landmarks for the face region, then
	# convert the facial landmark (x, y)-coordinates to a NumPy
	# shape = predictor(gray, rect)
	shape = predictor(image, rect)
	shape = face_utils.shape_to_np(shape)

	# loop over the (x, y)-coordinates for the facial landmarks
	# and draw them on the image
	print('image:',image.shape)
	for (x, y) in shape:
		cv2.line(images, (x, y), (x, y), (0, 0, 255), 5)

plt.imshow(images)
plt.xticks([])
plt.yticks([])
plt.title("Output")

fname = "results/"+"result_" + args["image"][1]

plt.savefig(fname)
plt.show()


