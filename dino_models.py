
'''
Create classes for each bit dino
The classes are inherited from the base model which picks the colors for different parts and accesories

TODO:
need to store the accessories info and return it to generate.py

'''
from random import randint, sample

import numpy as np

from base_model import base_model


class dino_1(base_model):

    def __init__(self, seedID, tier):
        super().__init__(seedID,tier)

    def get_dino(self):
        # base
        bb = self.b
        oo = self.o
        ss = self.s
        hh = self.h
        ww = self.w
        ee = self.e
        dd = self.d    

        # accessories

        dino =     [[bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,oo,oo,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,oo,ss,ss,ss,oo,oo,oo,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,oo,oo,oo,oo,oo,ss,ss,ss,ss,ss,ss,oo,oo,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,hh,hh,hh,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,hh,hh,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb],
                    [bb,bb,bb,bb,bb,oo,oo,hh,oo,ss,ss,ss,ss,ss,ss,ww,ww,ss,ss,ss,ss,oo,oo,bb],
                    [bb,bb,bb,bb,bb,bb,oo,oo,oo,ss,ss,ss,ss,ss,ss,ww,ee,ss,ss,ss,ss,ss,oo,bb],
                    [bb,bb,bb,bb,bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb],
                    [bb,bb,bb,oo,oo,oo,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb],
                    [bb,bb,oo,hh,hh,hh,oo,ss,ss,ss,ss,ss,ss,oo,oo,oo,oo,oo,oo,oo,oo,oo,oo,bb],
                    [bb,bb,oo,hh,hh,hh,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb,bb],
                    [bb,bb,oo,hh,hh,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,oo,oo,oo,bb,bb,bb],
                    [bb,bb,oo,oo,hh,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,dd,oo,bb,bb,bb,bb,bb,bb,bb],
                    [oo,oo,oo,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,dd,dd,dd,oo,bb,bb,bb,bb,bb,bb],
                    [hh,hh,hh,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,dd,dd,dd,dd,oo,bb,bb,bb,bb,bb],
                    [hh,hh,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,dd,dd,dd,dd,dd,dd,oo,bb,bb,bb,bb],
                    [hh,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,dd,dd,dd,dd,dd,dd,dd,dd,oo,bb,bb,bb],
                    [oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,dd,dd,dd,dd,dd,dd,dd,dd,dd,dd,oo,bb,bb]]

        return dino

    def get_mask(self):
        # mask
        bb = 255
        oo = ss = hh = ww = ee = dd = 0  

        mask =     [[bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,oo,oo,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,oo,ss,ss,ss,oo,oo,oo,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,oo,oo,oo,oo,oo,ss,ss,ss,ss,ss,ss,oo,oo,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,hh,hh,hh,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,hh,hh,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb],
                    [bb,bb,bb,bb,bb,oo,oo,hh,oo,ss,ss,ss,ss,ss,ss,ww,ww,ss,ss,ss,ss,oo,oo,bb],
                    [bb,bb,bb,bb,bb,bb,oo,oo,oo,ss,ss,ss,ss,ss,ss,ww,ee,ss,ss,ss,ss,ss,oo,bb],
                    [bb,bb,bb,bb,bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb],
                    [bb,bb,bb,oo,oo,oo,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb],
                    [bb,bb,oo,hh,hh,hh,oo,ss,ss,ss,ss,ss,ss,oo,oo,oo,oo,oo,oo,oo,oo,oo,oo,bb],
                    [bb,bb,oo,hh,hh,hh,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb,bb],
                    [bb,bb,oo,hh,hh,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,oo,oo,oo,bb,bb,bb],
                    [bb,bb,oo,oo,hh,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,dd,oo,bb,bb,bb,bb,bb,bb,bb],
                    [oo,oo,oo,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,dd,dd,dd,oo,bb,bb,bb,bb,bb,bb],
                    [hh,hh,hh,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,dd,dd,dd,dd,oo,bb,bb,bb,bb,bb],
                    [hh,hh,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,dd,dd,dd,dd,dd,dd,oo,bb,bb,bb,bb],
                    [hh,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,dd,dd,dd,dd,dd,dd,dd,dd,oo,bb,bb,bb],
                    [oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,dd,dd,dd,dd,dd,dd,dd,dd,dd,dd,oo,bb,bb]]
        return mask

class dino_2(base_model):

    def __init__(self, seedID, tier):
        super().__init__(seedID, tier)


    def get_dino(self):
        # base
        bb = self.b
        oo = self.o
        ss = self.s
        dd = self.d

        # accessories
        sd = [ss,(153,204,255)] # drool  
        st = [ss,(63, 81, 181)] # vein
        hh = [bb,self.h] # hat
        ee = self.e # crazy eye

        accessories = {'drool': sd,     # drool
                       'vein': st,      # vein
                       'hat': hh,       # hat
                       'crazy eye': ee # crazy eye
                    }

        [sd,st,hh,ee] = self.select_accessories(accessories)

        if self.tier == 'legendary':
            hh = bb

        dino =     [[bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,hh,hh,hh,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,hh,hh,hh,hh,hh,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,hh,hh,hh,hh,hh,hh,hh,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,oo,oo,oo,oo,oo,oo,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,oo,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,oo,oo,ss,ss,ss,oo,ss,ss,ss,ss,oo,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,oo,ee,oo,ss,ss,oo,ee,oo,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,st,oo,ss,ss,ss,ss,oo,ss,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,st,ss,ss,st,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,oo,bb,bb,bb],
                    [bb,bb,oo,ss,ss,st,ss,ss,st,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb],
                    [bb,bb,oo,oo,ss,st,ss,st,ss,ss,ss,ss,oo,ss,ss,ss,ss,oo,ss,oo,ss,oo,bb,bb],
                    [bb,bb,bb,oo,ss,ss,st,ss,ss,ss,ss,sd,sd,oo,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb],
                    [bb,bb,bb,oo,ss,ss,st,ss,ss,ss,ss,ss,sd,sd,oo,oo,ss,ss,ss,ss,ss,oo,bb,bb],
                    [bb,bb,bb,oo,oo,st,ss,ss,ss,ss,ss,ss,ss,sd,sd,oo,oo,oo,oo,oo,oo,oo,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,sd,ss,oo,oo,oo,oo,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,sd,ss,ss,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,sd,ss,oo,oo,bb,oo,oo,oo,oo,oo,bb,bb],
                    [bb,bb,bb,oo,oo,ss,ss,ss,dd,dd,dd,ss,ss,sd,oo,oo,oo,oo,oo,oo,oo,oo,bb,bb],
                    [bb,bb,bb,oo,ss,ss,ss,ss,dd,dd,dd,ss,ss,ss,ss,oo,oo,oo,oo,oo,bb,oo,bb,bb],
                    [bb,bb,oo,oo,ss,ss,ss,dd,dd,dd,dd,dd,ss,ss,ss,ss,oo,bb,bb,oo,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,dd,dd,dd,dd,dd,dd,dd,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb]]

        if self.tier == 'legendary':
            dino = self.add_crown(dino)

        return dino

    def add_crown(self, dino, MASK = False):
        """
        overwrite pixels on dino to add a yellow crown
        :param dino: 24 * 24 dino array
        :return: modified dino array
        """
        dino = np.array(dino)
        if MASK == False:
            pixel = self.crown_yellow
        
        elif MASK == True:
            pixel = 0
        
        dino[0, 10] = pixel
        dino[1, 6] = pixel
        dino[1, 9:11] = pixel
        dino[1, 13] = pixel
        dino[2, 6:8] = pixel
        dino[2, 9:11] = pixel
        dino[2, 12:14] = pixel
        dino[3, 7:13] = pixel

        self.properties['crown'] = 1

        return dino


    def get_mask(self):

        bb = 255

        oo = ss = ee = dd = st = sd = 0

        if self.properties['hat'] == 1:
            hh = 0
        else:
            hh = 255

        mask =     [[bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,hh,hh,hh,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,hh,hh,hh,hh,hh,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,hh,hh,hh,hh,hh,hh,hh,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,oo,oo,oo,oo,oo,oo,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,oo,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,oo,oo,ss,ss,ss,oo,ss,ss,ss,ss,oo,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,oo,ee,oo,ss,ss,oo,ee,oo,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,st,oo,ss,ss,ss,ss,oo,ss,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,st,ss,ss,st,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,oo,bb,bb,bb],
                    [bb,bb,oo,ss,ss,st,ss,ss,st,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb],
                    [bb,bb,oo,oo,ss,st,ss,st,ss,ss,ss,ss,oo,ss,ss,ss,ss,oo,ss,oo,ss,oo,bb,bb],
                    [bb,bb,bb,oo,ss,ss,st,ss,ss,ss,ss,sd,sd,oo,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb],
                    [bb,bb,bb,oo,ss,ss,st,ss,ss,ss,ss,ss,sd,sd,oo,oo,ss,ss,ss,ss,ss,oo,bb,bb],
                    [bb,bb,bb,oo,oo,st,ss,ss,ss,ss,ss,ss,ss,sd,sd,oo,oo,oo,oo,oo,oo,oo,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,sd,ss,oo,oo,oo,oo,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,sd,ss,ss,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,sd,ss,oo,oo,bb,oo,oo,oo,oo,oo,bb,bb],
                    [bb,bb,bb,oo,oo,ss,ss,ss,dd,dd,dd,ss,ss,sd,oo,oo,oo,oo,oo,oo,oo,oo,bb,bb],
                    [bb,bb,bb,oo,ss,ss,ss,ss,dd,dd,dd,ss,ss,ss,ss,oo,oo,oo,oo,oo,bb,oo,bb,bb],
                    [bb,bb,oo,oo,ss,ss,ss,dd,dd,dd,dd,dd,ss,ss,ss,ss,oo,bb,bb,oo,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,dd,dd,dd,dd,dd,dd,dd,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb]]  

        if self.tier == 'legendary':
            mask = self.add_crown(mask,MASK=True)

        return mask


class dino_3(base_model):

    def __init__(self, seedID, tier):
        super().__init__(seedID, tier)

    def get_dino(self):
        # base
        bb = self.b
        oo = self.o
        ss = self.s
        ww = self.w
        ee = self.e
        gg = (255,153,153) # pink red

        # accessories
        cs = [ss,(102,178,255)] 
        lo = [ss,(102,178,255)]
 

        accessories = {'drool': lo,     # drool
                       'cry': cs,      # vein
                       'crazy eye': ee # crazy eye
                    }

        [lo,cs,ee] = self.select_accessories(accessories)

        dino =     [[bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb], 
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb], 
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,oo,oo,oo,oo,bb,bb,bb,bb,bb,bb,bb], 
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,ss,ss,ss,ss,ss,oo,oo,oo,bb,bb,bb,bb], 
                    [bb,bb,bb,bb,bb,bb,bb,bb,oo,oo,oo,oo,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb,bb], 
                    [bb,bb,bb,bb,bb,oo,oo,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,ss,oo,bb,bb,bb], 
                    [bb,bb,bb,bb,oo,oo,ss,ss,ss,ss,oo,oo,ss,ss,ss,ss,ss,ss,oo,ss,oo,oo,bb,bb], 
                    [bb,bb,bb,bb,oo,ss,ss,ss,oo,oo,oo,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb], 
                    [bb,bb,bb,oo,oo,ss,ss,ss,ss,oo,ee,oo,ss,ss,ss,ss,ss,ss,ss,oo,oo,oo,bb,bb], 
                    [bb,bb,bb,oo,ss,ss,ss,cs,cs,oo,ww,oo,ss,ss,ss,ss,ss,ss,oo,oo,ww,bb,bb,bb], 
                    [bb,bb,oo,ss,ss,ss,ss,cs,cs,cs,oo,oo,ss,ss,ss,ss,ss,oo,oo,ww,ww,bb,bb,bb], 
                    [bb,oo,oo,ss,ss,ss,ss,ss,cs,cs,ss,ss,ss,ss,ss,ss,oo,oo,ww,bb,ww,bb,ww,bb], 
                    [bb,oo,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,ss,ss,oo,oo,ww,ww,bb,bb,ww,ww,bb], 
                    [oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,oo,ww,bb,ww,bb,ww,oo,oo,bb], 
                    [oo,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,oo,ww,ww,ww,bb,bb,ww,oo,ss,oo,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,oo,gg,ww,bb,bb,ww,oo,oo,ss,ss,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,lo,lo,gg,gg,gg,ww,oo,oo,ss,ss,ss,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,lo,lo,lo,oo,oo,oo,oo,ss,ss,ss,ss,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,lo,lo,ss,ss,ss,ss,ss,ss,ss,oo,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,lo,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,lo,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,lo,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,lo,ss,ss,ss,ss,oo,oo,oo,bb,bb,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,lo,oo,oo,oo,oo,oo,bb,bb,bb,bb,bb]]

        if self.tier == 'legendary':
            dino = self.add_crown(dino)

        return dino
    

    def add_crown(self, dino, MASK = False):
        """
        overwrite pixels on dino to add a yellow crown
        :param dino: 24 * 24 dino array
        :return: modified dino array
        """
        dino = np.array(dino)
        if MASK == False:
            pixel = self.crown_yellow
        
        elif MASK == True:
            pixel = 0
        
        dino[1,2:4] = pixel
        dino[2,3:5] = pixel
        dino[3, 3:6] = pixel
        dino[4, 0:2] = pixel
        dino[4, 4:7] = pixel
        dino[5, 1:5] = pixel
        dino[6, 2:4] = pixel
        dino[7, 3] = pixel
        dino[8, 0:3] = pixel
        dino[9, 1:3] = pixel

        self.properties['crown'] = 1

        return dino


    def get_mask(self):
        # base
        bb = 255
        oo = ss = ww = ee = gg = cs = lo = 0

        mask =     [[bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb], 
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb], 
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,oo,oo,oo,oo,bb,bb,bb,bb,bb,bb,bb], 
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,ss,ss,ss,ss,ss,oo,oo,oo,bb,bb,bb,bb], 
                    [bb,bb,bb,bb,bb,bb,bb,bb,oo,oo,oo,oo,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb,bb], 
                    [bb,bb,bb,bb,bb,oo,oo,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,ss,oo,bb,bb,bb], 
                    [bb,bb,bb,bb,oo,oo,ss,ss,ss,ss,oo,oo,ss,ss,ss,ss,ss,ss,oo,ss,oo,oo,bb,bb], 
                    [bb,bb,bb,bb,oo,ss,ss,ss,oo,oo,oo,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb], 
                    [bb,bb,bb,oo,oo,ss,ss,ss,ss,oo,ee,oo,ss,ss,ss,ss,ss,ss,ss,oo,oo,oo,bb,bb], 
                    [bb,bb,bb,oo,ss,ss,ss,cs,cs,oo,ww,oo,ss,ss,ss,ss,ss,ss,oo,oo,ww,bb,bb,bb], 
                    [bb,bb,oo,ss,ss,ss,ss,cs,cs,cs,oo,oo,ss,ss,ss,ss,ss,oo,oo,ww,ww,bb,bb,bb], 
                    [bb,oo,oo,ss,ss,ss,ss,ss,cs,cs,ss,ss,ss,ss,ss,ss,oo,oo,ww,bb,ww,bb,ww,bb], 
                    [bb,oo,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,ss,ss,oo,oo,ww,ww,bb,bb,ww,ww,bb], 
                    [oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,oo,ww,bb,ww,bb,ww,oo,oo,bb], 
                    [oo,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,oo,ww,ww,ww,bb,bb,ww,oo,ss,oo,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,oo,gg,ww,bb,bb,ww,oo,oo,ss,ss,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,lo,lo,gg,gg,gg,ww,oo,oo,ss,ss,ss,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,lo,lo,lo,oo,oo,oo,oo,ss,ss,ss,ss,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,lo,lo,ss,ss,ss,ss,ss,ss,ss,oo,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,lo,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,lo,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,lo,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,lo,ss,ss,ss,ss,oo,oo,oo,bb,bb,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,lo,oo,oo,oo,oo,oo,bb,bb,bb,bb,bb]]
        
        if self.tier == 'legendary':
            mask = self.add_crown(mask,MASK=True)
        
        return mask


class dino_4(base_model):

    def __init__(self, seedID, tier):
        super().__init__(seedID, tier)

    def get_dino(self):
        # base
        bb = self.b
        oo = self.o
        ss = self.s
        ww = self.w
        ee = self.e
        dd = self.d
        pp = (ss[0]+10,ss[1]+10,ss[2]+10)
        zz = (dd[0]+10,dd[1]+10,dd[2]+10)

        dino =     [[bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,ww,ww,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,ww,ww,ww,ww,oo,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,oo,oo,oo,pp,pp,ww,ww,pp,pp,oo,oo,oo,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,pp,pp,pp,ss,pp,ww,ww,pp,ss,pp,pp,pp,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,oo,pp,pp,pp,pp,pp,pp,pp,pp,pp,pp,oo,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,oo,pp,pp,pp,pp,pp,pp,pp,pp,pp,pp,oo,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,pp,pp,pp,pp,pp,pp,pp,pp,pp,pp,ss,oo,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,ss,pp,pp,pp,pp,pp,pp,pp,pp,ss,ss,oo,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,ss,ww,ee,pp,ww,pp,pp,ww,pp,ee,ww,ss,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,ss,ww,ee,oo,ww,pp,pp,ww,oo,ee,ww,ss,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,oo,pp,oo,ss,pp,pp,pp,pp,pp,pp,pp,pp,ss,oo,ss,oo,oo,bb,bb,bb],
                    [bb,bb,bb,oo,pp,pp,oo,ss,ss,pp,pp,pp,pp,pp,pp,ss,ss,oo,pp,pp,oo,bb,bb,bb],
                    [bb,bb,oo,pp,pp,pp,ss,oo,ss,ss,oo,ss,ss,oo,ss,ss,oo,ss,pp,pp,pp,oo,bb,bb],
                    [bb,bb,oo,pp,pp,pp,ss,dd,oo,oo,zz,zz,zz,zz,oo,oo,dd,ss,ss,pp,pp,ss,oo,bb],
                    [bb,oo,ss,pp,pp,ss,ss,dd,zz,dd,oo,oo,oo,oo,dd,zz,dd,ss,oo,ss,ss,ww,oo,bb],
                    [bb,oo,ww,ss,ss,oo,dd,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,dd,oo,ww,oo,oo,bb,bb],
                    [bb,bb,oo,oo,ww,oo,oo,dd,dd,zz,zz,zz,zz,zz,zz,zz,zz,oo,ss,oo,oo,bb,bb,bb],
                    [bb,bb,bb,oo,oo,pp,pp,dd,dd,zz,zz,zz,zz,zz,zz,dd,dd,dd,pp,oo,bb,bb,bb,bb],
                    [bb,bb,bb,oo,pp,pp,pp,dd,dd,dd,dd,dd,dd,dd,dd,dd,dd,pp,pp,pp,oo,bb,bb,bb],
                    [bb,bb,bb,oo,ss,pp,pp,ss,oo,dd,dd,dd,dd,dd,dd,dd,ss,pp,pp,pp,oo,bb,bb,bb],
                    [bb,bb,bb,bb,oo,ss,ss,ss,oo,oo,dd,dd,dd,dd,oo,ss,ss,pp,pp,ss,oo,bb,bb,bb],
                    [bb,bb,bb,bb,oo,ww,ww,ss,oo,bb,oo,oo,oo,oo,oo,ss,ss,ss,ss,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,oo,oo,bb,bb,bb,bb,bb,bb,bb,oo,ss,ww,ww,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,oo,oo,bb,bb,bb,bb,bb]]

        # accessories
        dino = np.array(dino)

        if self.properties['crazyeye']:
            dino = self.add_crazy_eye(dino)

        if self.properties['sunglasses']:
            dino = self.add_sunglasses(dino)

        if self.properties['crown']:
            dino = self.add_crown(dino)

        return dino

    def get_mask(self):
        # base
        bb = 255
        oo = ss = ww = ee = dd = pp = zz = 0

        # accessories

        mask =     [[bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,ww,ww,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,ww,ww,ww,ww,oo,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,oo,oo,oo,pp,pp,ww,ww,pp,pp,oo,oo,oo,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,pp,pp,pp,ss,pp,ww,ww,pp,ss,pp,pp,pp,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,oo,pp,pp,pp,pp,pp,pp,pp,pp,pp,pp,oo,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,oo,pp,pp,pp,pp,pp,pp,pp,pp,pp,pp,oo,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,pp,pp,pp,pp,pp,pp,pp,pp,pp,pp,ss,oo,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,ss,pp,pp,pp,pp,pp,pp,pp,pp,ss,ss,oo,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,ss,ee,ww,pp,ee,pp,pp,ee,pp,ww,ee,ss,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,ss,ee,ww,oo,ee,pp,pp,ee,oo,ww,ee,ss,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,oo,pp,oo,ss,pp,pp,pp,pp,pp,pp,pp,pp,ss,oo,ss,oo,oo,bb,bb,bb],
                    [bb,bb,bb,oo,pp,pp,oo,ss,ss,pp,pp,pp,pp,pp,pp,ss,ss,oo,pp,pp,oo,bb,bb,bb],
                    [bb,bb,oo,pp,pp,pp,ss,oo,ss,ss,oo,ss,ss,oo,ss,ss,oo,ss,pp,pp,pp,oo,bb,bb],
                    [bb,bb,oo,pp,pp,pp,ss,dd,oo,oo,zz,zz,zz,zz,oo,oo,dd,ss,ss,pp,pp,ss,oo,bb],
                    [bb,oo,ss,pp,pp,ss,ss,dd,zz,dd,oo,oo,oo,oo,dd,zz,dd,ss,oo,ss,ss,ww,oo,bb],
                    [bb,oo,ww,ss,ss,oo,dd,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,dd,oo,ww,oo,oo,bb,bb],
                    [bb,bb,oo,oo,ww,oo,oo,dd,dd,zz,zz,zz,zz,zz,zz,zz,zz,oo,ss,oo,oo,bb,bb,bb],
                    [bb,bb,bb,oo,oo,pp,pp,dd,dd,zz,zz,zz,zz,zz,zz,dd,dd,dd,pp,oo,bb,bb,bb,bb],
                    [bb,bb,bb,oo,pp,pp,pp,dd,dd,dd,dd,dd,dd,dd,dd,dd,dd,pp,pp,pp,oo,bb,bb,bb],
                    [bb,bb,bb,oo,ss,pp,pp,ss,oo,dd,dd,dd,dd,dd,dd,dd,ss,pp,pp,pp,oo,bb,bb,bb],
                    [bb,bb,bb,bb,oo,ss,ss,ss,oo,oo,dd,dd,dd,dd,oo,ss,ss,pp,pp,ss,oo,bb,bb,bb],
                    [bb,bb,bb,bb,oo,ww,ww,ss,oo,bb,oo,oo,oo,oo,oo,ss,ss,ss,ss,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,oo,oo,bb,bb,bb,bb,bb,bb,bb,oo,ss,ww,ww,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,oo,oo,bb,bb,bb,bb,bb]]

        if self.properties['crown']:
            mask = [[bb,bb,bb,bb,bb,bb,bb,bb,bb,ww,bb,ww,ww,bb,ww,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,ww,ww,ww,ww,oo,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,oo,oo,oo,pp,pp,ww,ww,pp,pp,oo,oo,oo,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,pp,pp,pp,ss,pp,ww,ww,pp,ss,pp,pp,pp,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,oo,pp,pp,pp,pp,pp,pp,pp,pp,pp,pp,oo,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,oo,pp,pp,pp,pp,pp,pp,pp,pp,pp,pp,oo,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,pp,pp,pp,pp,pp,pp,pp,pp,pp,pp,ss,oo,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,ss,pp,pp,pp,pp,pp,pp,pp,pp,ss,ss,oo,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,ss,ee,ww,pp,ee,pp,pp,ee,pp,ww,ee,ss,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,ss,ee,ww,oo,ee,pp,pp,ee,oo,ww,ee,ss,oo,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,oo,pp,oo,ss,pp,pp,pp,pp,pp,pp,pp,pp,ss,oo,ss,oo,oo,bb,bb,bb],
                    [bb,bb,bb,oo,pp,pp,oo,ss,ss,pp,pp,pp,pp,pp,pp,ss,ss,oo,pp,pp,oo,bb,bb,bb],
                    [bb,bb,oo,pp,pp,pp,ss,oo,ss,ss,oo,ss,ss,oo,ss,ss,oo,ss,pp,pp,pp,oo,bb,bb],
                    [bb,bb,oo,pp,pp,pp,ss,dd,oo,oo,zz,zz,zz,zz,oo,oo,dd,ss,ss,pp,pp,ss,oo,bb],
                    [bb,oo,ss,pp,pp,ss,ss,dd,zz,dd,oo,oo,oo,oo,dd,zz,dd,ss,oo,ss,ss,ww,oo,bb],
                    [bb,oo,ww,ss,ss,oo,dd,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,dd,oo,ww,oo,oo,bb,bb],
                    [bb,bb,oo,oo,ww,oo,oo,dd,dd,zz,zz,zz,zz,zz,zz,zz,zz,oo,ss,oo,oo,bb,bb,bb],
                    [bb,bb,bb,oo,oo,pp,pp,dd,dd,zz,zz,zz,zz,zz,zz,dd,dd,dd,pp,oo,bb,bb,bb,bb],
                    [bb,bb,bb,oo,pp,pp,pp,dd,dd,dd,dd,dd,dd,dd,dd,dd,dd,pp,pp,pp,oo,bb,bb,bb],
                    [bb,bb,bb,oo,ss,pp,pp,ss,oo,dd,dd,dd,dd,dd,dd,dd,ss,pp,pp,pp,oo,bb,bb,bb],
                    [bb,bb,bb,bb,oo,ss,ss,ss,oo,oo,dd,dd,dd,dd,oo,ss,ss,pp,pp,ss,oo,bb,bb,bb],
                    [bb,bb,bb,bb,oo,ww,ww,ss,oo,bb,oo,oo,oo,oo,oo,ss,ss,ss,ss,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,oo,oo,bb,bb,bb,bb,bb,bb,bb,oo,ss,ww,ww,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,oo,oo,oo,bb,bb,bb,bb,bb]]

        return mask

    def add_crazy_eye(self, dino):
        """
        overwrite pupil from black to crazyeye color
        :param dino:
        :return:
        """
        dino[9, 9] = (183, 28, 28)
        dino[9, 14] = (183, 28, 28)
        return dino

    def add_sunglasses(self, dino):
        """
        overwrite pixels on dino to add a pair of sunglasses that is black with white reflections
        :param dino: 24 * 24 dino array
        :return: modified dino array
        """
        # main body - black
        # first row
        dino[7, 6:18] = self.o
        # second row
        dino[8, 6:10] = self.o
        dino[8, 13:18] = self.o
        # thrid row
        dino[9, 7:11] = self.o
        dino[9, 13:17] = self.o
        # reflection - white
        dino[8, 10] = self.w
        dino[8, 16] = self.w
        dino[9, 9] = self.w
        dino[9, 15] = self.w

        return dino

    def add_crown(self, dino):
        """
        overwrite pixels on dino to add a yellow crown
        :param dino: 24 * 24 dino array
        :return: modified dino array
        """

        dino[0, 9] = self.crown_yellow
        dino[0, 11:13] = self.crown_yellow
        dino[0, 14] = self.crown_yellow

        dino[1, 9:15] = self.crown_yellow
        dino[2, 9:15] = self.crown_yellow

        return dino


