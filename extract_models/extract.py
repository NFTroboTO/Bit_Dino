import cv2
import numpy as np
from PIL import Image
import glob
import os

'''
Input: 24x24x3 pixel image

Output: string that represent the pixels
'''

image_list = {}
for filename in glob.glob('base_models/*.png'):
    #image = Image.open(filename)
    image = cv2.imread(filename)
    filename = os.path.basename(filename)
    filename = os.path.splitext(filename)[0]
    image_list[filename] = image

print(image_list.keys())

for key in image_list:
    image = image_list[key]
    width, height = image.shape[0:2]
    
    # initialize a dict to store pixel values
    pixel = {}

    # set a counter to count the number of diffent pixel values
    n = 0

    # set output array
    output = np.zeros((width,height))

    for x in range(width):
        for y in range(height):
            
            if pixel == {}:
                output[y,x] = n
                pixel[str(image[y,x])] = n

            if str(image[y,x]) not in pixel:
                n+=1
                pixel[str(image[y,x])] = n
                output[y,x] = n
            else:
                output[y,x] = pixel[str(image[y,x])]

    print(key)
    print(str(output.astype(int).tolist()))


    
