from django.shortcuts import render
from django.http import HttpResponse
import urllib
import cv2
import numpy as np

def index(request):
    return render(request, 'index.html')
    #return render(request, '/home/ebenezer/DAS/projectDas/core/templates/index.html')

#class FaceDetection(View):

#	processFaces(imageFromURL())
#	
#	def imageFromURL():
   	# Request URL to user
#    	url = raw_input('Insere a URL:')

    	# Get content of URL
 #   	url_response = urllib.urlopen(url)

    	# Convert into a numpy array
#    	image_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
#    	imageCode = cv2.imdecode(image_array, -1)

#    	file = "test_image_URL.png"
#    	cv2.imwrite(file, imageCode)

#    	imageCode = file
#    	return imageCode

#    def processFaces(object):
    	# Directory with the classifier for the facesFrontais
#    	faceCascade = cv2.CascadeClassifier('core/haarcascade_frontalface_default.xml')
#    	image = cv2.imread(object)
#    	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    	# Detect objects in the picture
#    	faces = faceCascade.detectMultiScale(
#        	gray,
#        	scaleFactor=1.1,
#        	minNeighbors=5,
#        	minSize=(20, 20),
#        	flags = cv2.CASCADE_SCALE_IMAGE
#    	)

    	# Print amount faces found
#   	print "Encontradas {0} faces!".format(len(faces))

    	# Draw retangle in around faces
#   	for (x, y, w, h) in faces:
#       	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
#   	cv2.imshow('Imagem', image)
#   	return cv2.waitKey()

def contact(request):
	return render(request, 'contact.html')
