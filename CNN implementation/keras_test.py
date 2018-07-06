from keras.models import load_model
from keras.preprocessing import image
#from keras.utils import plot_model
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #To solve the unoptimized problem.
# dimensions of our images
img_width, img_height = 300, 300

# load the model we saved
model = load_model('net.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
#plot_model(model, to_file='model.png')

photos_fld = './data/test/'
photos_to_test = ['1_10.jpg','2_10.jpg', '2_11.jpg', '4_5.JPG']
# predicting images
for photo in photos_to_test:
	img = image.load_img(photos_fld + photo, target_size=(img_width, img_height))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	images = np.vstack([x])
	classes = model.predict_classes(images, batch_size=10)
	print("For image: " + photo + " predicted class: " + str(classes))