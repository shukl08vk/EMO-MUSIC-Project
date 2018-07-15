import cv2
import sys
import json
import time
import numpy as np
from keras.models import model_from_json
d=[]
d1=[]
def fun(str):

	emotion_labels = ['angry', 'fear', 'happy', 'sad', 'surprise', 'neutral']
	cascPath = str

	faceCascade = cv2.CascadeClassifier(cascPath)

	# load json and create model arch
	json_file = open('model.json','r')
	loaded_model_json = json_file.read()
	json_file.close()
	model = model_from_json(loaded_model_json)

	# load weights into new model
	model.load_weights('model.h5')
	count=0
	def overlay_memeface(probs):
		if max(probs) > 0.6:
			emotion = emotion_labels[np.argmax(probs)]
			return (emotion)
		else:
			index1, index2 = np.argsort(probs)[::-1][:2]
			
			emotion1 = emotion_labels[index1]
			emotion2 = emotion_labels[index2]
			
			return(emotion2)
			
		

	def predict_emotion(face_image_gray): # a single cropped face
		resized_img = cv2.resize(face_image_gray, (48,48), interpolation = cv2.INTER_AREA)
		# cv2.imwrite(str(index)+'.png', resized_img)
		image = resized_img.reshape(1, 1, 48, 48)
		list_of_list = model.predict(image, batch_size=1, verbose=1)
		angry, fear, happy, sad, surprise, neutral = [prob for lst in list_of_list for prob in lst]
		a=overlay_memeface([angry, fear, happy, sad, surprise, neutral])
		return a

	
	while(count<1):
		# Capture frame-by-frame
		frame=cv2.imread("image1.png",1)
		img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY,1)
		count+=1

		faces = faceCascade.detectMultiScale(
			img_gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30),
			flags=cv2.CASCADE_SCALE_IMAGE
		)

		emotions = []
		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			d3=[]
			face_image_gray = img_gray[y:y+h, x:x+w]

			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			d3.append([(predict_emotion(face_image_gray))])


		# Display the resulting frame

		return(d3)
	# When everything is done, release the capture
	
	
#fun("haarcascade_frontalface_default.xml")
