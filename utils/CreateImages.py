import cv2
import numpy as np

data = np.load("C:/Users/programmer/Desktop/CHROMDINO/data/training_data.npy", allow_pickle=True)
targets = np.load("C:/Users/programmer/Desktop/CHROMDINO/data/target_data.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Lets see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Store both data and targets in a list.
# We may want to shuffle down the road.

holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

count = 0

for data in holder_list:
    #print(data[1])
    if data[1] == 'nothing':
        count += 1
        cv2.imwrite(f"C:/Users/programmer/Desktop/CHROMDINO/img/{count}n.png", data[0]) 
    elif data[1] == 'jump':
        count += 1
        cv2.imwrite(f"C:/Users/programmer/Desktop/CHROMDINO/img/{count}j.png", data[0]) 
    elif data[1] == 'duck':
        count += 1
        cv2.imwrite(f"C:/Users/programmer/Desktop/CHROMDINO/img/{count}d.png", data[0])
    elif data[1] == 'end':
        count += 1
        cv2.imwrite(f"C:/Users/programmer/Desktop/CHROMDINO/img/{count}e.png", data[0])  