import numpy as np
import cv2
import time
import os
import keyboard

from utils.grabscreen import grab_screen

file_name = "C:/Users/programmer/Desktop/CHROMDINO/data/training_data.npy"
file_name2 = "C:/Users/programmer/Desktop/CHROMDINO/data/target_data.npy"


def save_data(image_data, targets):
    np.save(file_name, image_data)
    np.save(file_name2, targets)


def get_data():

    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        image_data = list(np.load(file_name, allow_pickle=True))
        targets = list(np.load(file_name2, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        image_data = []
        targets = []
    return image_data, targets


image_data, targets = get_data()
time.sleep(5)

keyboard.press('space')
keyboard.release("space")

start = time.time()

ahead = 55
count = 0

white = True
pic = 1

while True:
    pic += 1
    last_time = time.time()
    image = grab_screen(region=(115, 415, 715, 500 ))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    action = "nothing"

    # Day Check
    if image[34][ahead] != image[34][ahead - 10] or image[40][ahead] != image[40][ahead - 10] or image[37][ahead] != image[37][ahead - 10]:
        #print("space")
        keyboard.release("down")
        keyboard.press("space")
        time.sleep(0.027)
        keyboard.release("space")
        action = "jump"
    # Check for birds!
    #elif np.all(image[0][55:80] < 255):
    elif image[0][ahead] != image[0][ahead - 10] and image[0][ahead+2] != image[0][ahead - 10] and image[0][ahead+4] != image[0][ahead - 10] and image[0][ahead+6] != image[0][ahead - 10] and image[0][ahead+8] != image[0][ahead - 10] and image[0][ahead+10] != image[0][ahead - 10] and image[0][ahead+12] != image[0][ahead - 10] and image[0][ahead+14] != image[0][ahead - 10]:
        print("down")
        keyboard.press("down")
        action = "duck"

    # Check for end game!
    elif np.all(image[7][350:390] < 255) and image[0][375] > 0:
        cv2.imwrite(f"END{count}.jpg", image)
        print("END")
        action = "end"
        image_data.append(image)
        targets.append(action)
        break

    image_data.append(image)
    targets.append(action)

    count += int(time.time() - start)

    if count > 218:
        count = 0
        start = time.time()
        #cv2.imwrite(f"test{count}.jpg", image)
        ahead += 1
        print(ahead)

    #cv2.imwrite(f"test{pic}.jpg", image)
save_data(image_data, targets)