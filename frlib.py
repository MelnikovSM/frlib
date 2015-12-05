import cv2, fnmatch
import os, time
import numpy as np

def captureFrame(device=0):
	camera=cv2.VideoCapture(device)
	for i in xrange(10):
		camera.read()
	timestamp = time.strftime("%Y%m%d-%H%M%S")
	_, image = camera.read()
	camera.release()
	image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	return image, timestamp

def cropFaces(image, cascade='/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml'):
	haar_faces = cv2.CascadeClassifier(cascade)
	faces = haar_faces.detectMultiScale(image, 
				scaleFactor=1.1, 
				minNeighbors=3, 
				minSize=(30, 30), 
				flags=cv2.CASCADE_SCALE_IMAGE)
	if not len(faces)==0:
		imgs=[]
		for face in faces:
			x, y, w, h = face
			crop_height = int((112 / float(92)) * w)
			midy = y + h/2
			y1 = max(0, midy-crop_height/2)
			y2 = min(image.shape[0]-1, midy+crop_height/2)
			imgs.append(cv2.resize(image[y1:y2, x:x+w], (92, 112), interpolation=cv2.INTER_LANCZOS4))
		return imgs

	else:
		return None

def genTemplate(dir, file):
	def walk_files(directory, match='*'):
		for root, dirs, files in os.walk(directory):
			for filename in fnmatch.filter(files, match):
				yield os.path.join(root, filename)
	def prepare_image(filename):
		return cv2.resize(cv2.imread(filename, cv2.IMREAD_GRAYSCALE), (92, 112), interpolation=cv2.INTER_LANCZOS4)

	faces = []
	labels = []
	pos_count = 0
	neg_count = 0

	for filename in walk_files(dir+'/positive', '*.pgm'):
		faces.append(prepare_image(filename))
		pos_count += 1
		labels.append(0)

	for filename in walk_files(dir+'/negative', '*.pgm'):
		faces.append(prepare_image(filename))
		neg_count += 1
		labels.append(1)

	model = cv2.createFisherFaceRecognizer()
	model.train(faces, np.asarray(labels))
	model.save(file)


def createRecognizer(templatefile):
	model = cv2.createFisherFaceRecognizer()
	model.load(templatefile)
	def recognizer(img):
		label, confidence = model.predict(img)
		return confidence, label
	return recognizer