import csv
from dino_models import dino_1
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

from dino_models import dino_1,dino_2,dino_3,dino_4



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

print('Bit Dino 1...')
# random generate 5 dino
for i in range(0,5):

    seedID = 1704+i*3

    if i < 30:
        tier = 'common'
    elif i < 43:
        tier = 'rare'
    elif i < 49:
        tier = 'epic'
    elif i == 49:
        tier = 'legendary'

    # convert the pixels into an array using numpy
    pixels =  dino_1(seedID,tier)# can use (random) to select different dino in the future
    pixelDino = np.array(pixels.dino, dtype=np.uint8)

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
        imgname = '../pixel_dinos/dino_1/' + md5.hexdigest() + '.png'
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


    ## Can modifiy the following code to generate certain colors for other parts         
    
    # # background color
    # f = randint(0, 1000)
    # if f > 500:
    #     # if random number is 501-1000 >> grey beak
    #     b = (152, 152, 152)
    #     background = 'grey'
    # elif 500 >= f > 47:
    #     # 48-500 >> gold beak
    #     b = (204, 172, 0)
    #     background = 'gold'
    # elif 47 >= f > 7:
    #     # 8 >> 47 >> red beak
    #     b = (204, 0, 0) 
    #     background = 'red'
    # else:
    #     # random number is 7 or less >> black beak
    #     b = (0, 0, 0) 
    #     background = 'black'


