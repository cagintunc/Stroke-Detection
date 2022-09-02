import os
import time
import uuid

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, Activation
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.optimizers import Adam
import cv2
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
import random


def model():
    model = Sequential([
        Conv2D(filters=16, kernel_size=(5, 5), input_shape=(224, 224, 3),
               activation="relu", padding="same"),
        MaxPooling2D(pool_size=(2, 2), strides=2),
        Conv2D(filters=32, kernel_size=(3, 3), activation="relu",
               padding="same"),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(filters=128, kernel_size=(3, 3), activation="relu", padding="same"),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.5),
        Dense(units=64, activation="relu"),
        Flatten(),
        Dropout(0.5),
        Dense(units=2, activation="softmax")
    ])
    model.compile(optimizer=Adam(learning_rate=.0001), loss="categorical_crossentropy",
                  metrics=["accuracy"])
    return model


def increase_data(train_or_valid, normal_or_stroke, data_number):
    print(f"FOR {normal_or_stroke.upper()}")
    path = "C:\\Users\\cagin\\OneDrive\\Masaüstü\\hackatone\\data"
    if train_or_valid == "train":
        path += "\\train"
    else:
        path += "\\val"

    if normal_or_stroke == "normal":
        path += "\\normal"
    else:
        path += "\\stroke"
    os.chdir(path)
    name_of_file = normal_or_stroke

    cap = cv2.VideoCapture(0)

    while data_number > 0:
        success, frame = cap.read()
        file_name = name_of_file + str(uuid.uuid1()) + ".jpg"
        print(file_name)
        print(path)
        cv2.imwrite(file_name, frame)
        print(os.path.exists(file_name))
        cv2.imshow("frame", frame)
        cv2.waitKey(0)
        data_number -= 1
    cap.release()
    cv2.destroyAllWindows()


physical_devices = tf.config.experimental.list_physical_devices("GPU")
print(f"Numbers of GPU {len(physical_devices)}")
tf.config.experimental.set_memory_growth(physical_devices[0], True)

train_path = "C:\\Users\\cagin\\OneDrive\\Masaüstü\\hackatone\\data\\train"
val_path = "C:\\Users\\cagin\\OneDrive\\Masaüstü\\hackatone\\data\\val"

train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet.preprocess_input)\
    .flow_from_directory(directory=train_path, target_size=(224, 224),
                         classes=["normal", "stroke"], batch_size=16)

val_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet.preprocess_input)\
    .flow_from_directory(directory=val_path, target_size=(224, 224),
                         classes=["normal", "stroke"], batch_size=16)

my_model = model()
my_model.fit(x=train_batches, validation_data=val_batches, epochs=80, verbose=2,)

if os.path.exists("model") is False:
    os.mkdir("model")

if os.path.exists("model\\model.h5") is False:
    my_model.save("model\\model.h5")

# increase_data("train", "stroke", 50)



