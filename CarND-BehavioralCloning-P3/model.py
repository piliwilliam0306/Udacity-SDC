import numpy as np
import keras
import cv2
import pickle
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from keras.models import *
from keras.layers import *
from keras.optimizers import Adam
#from keras.utils import plot_model
#from keras.utils.vis_utils import model_to_dot

#preprocessed training data
train_file = 'train.p'

#batch size and epoch
batch_size=128
epochs=25

if __name__ == '__main__':

	print("loading data")

	with open(train_file, mode='rb') as f:
		train = pickle.load(f)

	X_train, y_train = train['features'], train['labels']

	# split train and validation dataset
	X_train, y_train = shuffle(X_train, y_train)
	X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, random_state=0, test_size=0.15)

	# build model architecture

	model = Sequential([
			Lambda(lambda x: x/127.5 - 1.,input_shape=(14, 32, 1)),
			Conv2D(2, 3, 3, border_mode='valid', input_shape=(14, 32, 1), activation='relu'),
			MaxPooling2D((5, 5),(4, 4),'valid'),
			Dropout(0.25),
			Flatten(),
			Dense(1)
		])

	model.summary()
	#plot_model(model, to_file='model.png', show_shapes = True)
	earlyStopping=keras.callbacks.EarlyStopping(monitor='val_loss', 
                                            patience=2, min_delta=0.0001, 
                                            verbose=0, mode='auto')
	# training

	model.compile(loss='mse',optimizer=Adam(lr=1e-3))
	history = model.fit(X_train, y_train,batch_size=batch_size, 
						epochs=epochs, verbose=1, 
						validation_data=(X_val, y_val),
						callbacks=[earlyStopping])

	# save model
	model.save("model.h5")

	with open("model.json", "w") as json_file:
		json_file.write(model.to_json())

	print("Model Saved.")
