import csv
import hashlib
import os
import time
from random import randint, seed

import numpy as np
import requests
import webcolors
from PIL import Image
from webcolors import CSS3_HEX_TO_NAMES
import pandas as pd
from tabulate import tabulate

from base_models import base_models

'''
Helper Functions to set pixel colors for each part
'''

#########################################################################
# get closest named color from RGB value
def closest_colour(color):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - color[0]) ** 2
        gd = (g_c - color[1]) ** 2
        bd = (b_c - color[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = 'NA'
    return actual_name, closest_name

def set_part_color():
    # hat color - randomly generate rgb color
    r = randint(0, 256)
    g = randint(0, 256)
    b = randint(0, 256)
    rgb = (r,g,b)

    actual,closet = get_colour_name(rgb)

    return rgb, actual, closet
#########################################################################

'''
Initialize image parameters,
Load database to check duplicates
'''
dimensions = (1024, 1024)

# outline color
o = (0, 0, 0)

#teeth color
t = (255,255,255)

md5 = hashlib.md5() ###################IMPORTANT#####################

print("\n###############")
print("#Loading DB...#")
print("###############")

try:
    database = pd.read_csv('pixel_dino_database.csv')
except pd.errors.EmptyDataError:
    print("\nCSV file is empty...")
    database = []
    generated_dino = []
else:
    print("\nDatabase loaded successfully!")
    generated_dino = database['Image'].tolist()

'''
Generate pixel dino
'''

print("\n###############")
print("#Generating...#")
print("###############\n")
# random generate 5 dino
for i in range(0,5):

    seedID = 1704+i*3
    seed(seedID)

    # generate hat color
    h,hat_actual,hat_closest = set_part_color()

    # generate eye color
    e,eye_actual,eye_closest = set_part_color()

    # generate skin color
    s,skin_actual,skin_closest = set_part_color()

    # generate duzi color
    d,duzi_actual,duzi_closest = set_part_color()

    ## Can modifiy the following code to generate certain colors for other parts         
    
    # background color
    f = randint(0, 1000)
    if f > 500:
        # if random number is 501-1000 >> grey beak
        b = (152, 152, 152)
        background = 'grey'
    elif 500 >= f > 47:
        # 48-500 >> gold beak
        b = (204, 172, 0)
        background = 'gold'
    elif 47 >= f > 7:
        # 8 >> 47 >> red beak
        b = (204, 0, 0) 
        background = 'red'
    else:
        # random number is 7 or less >> black beak
        b = (0, 0, 0) 
        background = 'black'
    
    # initialize models 
    # p = (s[0]+20,s[1]+20,s[2]+20)
    # w = e
    # z = (d[0]+20,d[1]+20,d[2]+20)
    # dino = [2,[b,o,s,p,e,w,z,d]]
    dino = [3,[b,o,h,s,d]]
    models = base_models(dino)
    # convert the pixels into an array using numpy
    pixels = models.dino # can use (random) to select different dino in the future
    pixelDino = np.array(pixels, dtype=np.uint8)

    # Check with database, see if the current dino has already been generated or not
    md5.update(str(pixelDino).encode('utf-8'))
    
    if md5.hexdigest() in generated_dino:
        print("Duplicate["+md5.hexdigest()+']')
        continue
    else:
        current_dino = {'Image':md5.hexdigest(),'Generated':True,'Properties':['placeholder'],'Seed':seedID}
        database.append(current_dino)
        print('Current Bit Dino is generated: \ns')
        print(current_dino)
        # use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(pixelDino)
        new_image = new_image.resize(dimensions, resample=0)
        imgname = 'pixel_dinos/' + md5.hexdigest() + '.png'
        new_image.save(imgname)


print("\n##############")
print("#Completed!!!#")
print("##############\n")
'''
After generation is finished, save the generated pixel dino hash to database
'''
df = pd.DataFrame(database)
print(tabulate(df, headers='keys', tablefmt='psql'))

df.to_csv('pixel_dino_database.csv',index=False)



