from random import randint, seed, sample

import numpy as np
import webcolors
from PIL import Image

import cv2
'''
This class is meant to store the base models
Is imported in generate.py

b - background
h - hat
o - outline
s - skin
e - eye
t - teeth
d - du zi
.
.
.

'''

class base_model():
    
    def __init__(self, seedID, tier):

        # set random seed
        seed(seedID)

        # set output dimension
        self.dimension = (1440, 1440)

        # generate colors

        # backgound
        self.b = (0,0,0)
        # outline
        self.o = (0,0,0) # always black
        # white
        self.w = (255,255,255) # some parts always white, ie, teeth, eyewhite
        # skin
        self.s,self.s_actual,self.s_closet = self.set_part_color()
        # du zi
        self.d,self.d_actual,self.d_closet = self.set_part_color()
        # eye
        self.e = [(121, 85, 72), (255, 0, 0)] # normal eye and crazy eye
        # hat
        self.h,self.h_actual,self.h_closet = self.set_part_color()
        #...



        # Common: one of 1-3
        # Rare: Two of 1-3
        # Epic: Three of 1-4
        # Legendary: All of 2-5
        # self.accessories = ['crazyeye','hat','tattoo','sunglasses','crown']
        # self.properties = {'smoke':0,'cry':0,'drool':0,'crazyeye':0,'hat':0,'tattoo':0,'sunglasses':0,'crown':0}
        

        self.choose_tier(tier)


    def choose_tier(self,tier):

        if tier == 'common':
            self.bg = Image.open('backgrounds/common1.png')
            self.num_of_acc = 1

            #TODO:
            # choose accessories

        elif tier == 'rare':
            self.bg = Image.open('backgrounds/rare1.png')
            self.num_of_acc = 2

        elif tier == 'epic':
            self.bg = Image.open('backgrounds/epic1.png')
            self.num_of_acc = 3

        elif tier == 'legendary':

            self.bg = Image.open('backgrounds/legendary.png')
            self.num_of_acc = -1 # means every possible accessories


    def add_properties(self, accessories):

        properties = {} # init an empty dict for storing properties

        for acc in accessories:
            properties[acc] = 0

        return properties

    def select_accessories(self,accessories):

        # select self.num_of_acc accessories based on tier 
        accs = list(accessories.keys())
        
        if self.num_of_acc != -1:
            selected = sample(accs, self.num_of_acc)
        else:
            selected = accs # select all if tier is legendary

        self.properties = self.add_properties(accs)

        # set selected accessories
        for acc in selected:
            self.properties[acc] = 1

        # set accessories according to property dictionary        
        acc_pixel = []
        for acc in accs:
            curr_acc = accessories[acc][self.properties[acc]]
            acc_pixel.append(curr_acc)
        
        return acc_pixel

    def yes_or_no(self):

        return randint(0, 1) == 0

    '''
    Helper Functions to set pixel colors for each part
    '''
    #########################################################################
    # get closest named color from RGB value
    def closest_colour(self,color):
        min_colours = {}
        for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - color[0]) ** 2
            gd = (g_c - color[1]) ** 2
            bd = (b_c - color[2]) ** 2
            min_colours[(rd + gd + bd)] = name
        return min_colours[min(min_colours.keys())]

    def get_colour_name(self,requested_colour):
        try:
            closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
        except ValueError:
            closest_name = self.closest_colour(requested_colour)
            actual_name = 'NA'
        return actual_name, closest_name

    def set_part_color(self):
        # hat color - randomly generate rgb color
        r = randint(0, 256)
        g = randint(0, 256)
        b = randint(0, 256)
        rgb = (r,g,b)

        actual,closet = self.get_colour_name(rgb)

        # return alpha as well
        return (r,g,b), actual, closet
    #########################################################################


