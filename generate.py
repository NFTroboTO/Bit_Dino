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

md5 = hashlib.md5() ###################IMPORTANT#####################


root = "../pixel_dinos"
if not os.path.exists(root):
    os.mkdir(root)
datafile = root+'/pixel_dino_database.csv'

if not os.path.exists(datafile):
    with open(datafile, "w") as empty_csv:
        pass

print("\n###############")
print("#Loading DB...#")
print("###############")

try:
    database = pd.read_csv(datafile)
except pd.errors.EmptyDataError:
    print("\nCSV file is empty...")
    database = []
    generated_dino = []
else:
    print("\nDatabase loaded successfully!")
    generated_dino = database['Image'].tolist()
    database = database.to_dict(orient='records')

'''
Generate pixel dino
'''

print("\n###############")
print("#Generating...#")
print("###############\n")

seedID = 1704

dinos = [dino_1,dino_2,dino_3,dino_4]

for n,model in enumerate(dinos):

    dir = "../pixel_dinos/dino_"+str(n+1)

    if not os.path.exists(dir):
        os.mkdir(dir)

    print('Generating Bit Dino '+str(n+1) + ' ...')
    # random generate 5 dino
    for i in range(0,50):

        # skip common for dino 4
        if n == 3 and i < 30:
            continue

        seedID = seedID+i*3

        if i < 30:
            tier = 'common'
        elif i < 43:
            tier = 'rare'
        elif i < 49:
            tier = 'epic'
        elif i == 49:
            tier = 'legendary'

        # convert the pixels into an array using numpy
        bitdino =  model(seedID,tier)# can use (random) to select different dino in the future
        pixelDino = np.array(bitdino.get_dino(), dtype=np.uint8)
        mask = np.array(bitdino.get_mask(), dtype=np.uint8)
        bg = bitdino.bg
        # Check with database, see if the current dino has already been generated or not
        hashimage = pixelDino + np.array(bg)[:,:,:3]
        md5.update(str(hashimage).encode('utf-8'))
        
        if md5.hexdigest() in generated_dino:
            print("Duplicate["+md5.hexdigest()+']')
            continue
        else:
            # use PIL to create an image from the new array of pixels
            pixelDino = Image.fromarray(pixelDino)
            mask = Image.fromarray(mask)
            new_image = Image.composite(bg,pixelDino,mask)
            new_image = new_image.resize(bitdino.dimension, resample=0)
            imgname = dir+'/' + md5.hexdigest() + '.png'
            new_image.save(imgname)

            current_dino = {'Image':md5.hexdigest(),'Generated':True,'Properties':['placeholder'],'Seed':seedID}
            database.append(current_dino)
            print('Current Bit Dino is generated: \n')
            print(current_dino)

            

print("\n##############")
print("#Completed!!!#")
print("##############\n")
'''
After generation is finished, save the generated pixel dino hash to database
'''
df = pd.DataFrame(database)
print(tabulate(df, headers='keys', tablefmt='psql'))

df.to_csv(datafile,index=False)


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


