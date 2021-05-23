from random import randint, seed

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
    
    def __init__(self,seedID,tier):

        # set random seed
        seed(seedID)

        # set output dimension
        self.dimension = (1440, 1440)

        # generate colors

        # backgound
        self.b = [(224,224,224),(0,128,255),(153,0,153),(0,0,0)] #[grey, blue, purple, rainbow]
        # outline
        self.o = (0,0,0) # always black
        # white
        self.w = (255,255,255) # some parts always white, ie, teeth, eyewhite
        # skin
        self.s,self.s_actual,self.s_closet = self.set_part_color()
        # teeth
        self.t = self.w
        # du zi
        self.d,self.d_actual,self.d_closet = self.set_part_color()
        # eye
        e,_,_ = self.set_part_color()
        self.e = [e,(255,0,0)] # normal eye and crazy eye
        # hat
        self.h,self.h_actual,self.h_closet = self.set_part_color()
        #...

        self.bg = Image.open('test_bg/bg.png')
        #self.bg = np.array(bg)
        #self.bg = cv2.imread('test_bg/bg.png')

        red = (244,67,54)
        org = (255,152,0)
        yel = (255,235,59)
        gre = (204,255,144)
        dgr = (0,150,136)
        lbl = (0,188,212)
        blu = (33,150,243)
        pur = (103,58,183)

        self.rainbow = [[red,red,red,red,red,org,org,org,org,org,org,yel,yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre], 
                        [red,red,red,red,org,org,org,org,org,org,yel,yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr], 
                        [red,red,red,org,org,org,org,org,org,yel,yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr], 
                        [red,red,org,org,org,org,org,org,yel,yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr], 
                        [red,org,org,org,org,org,org,yel,yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr], 
                        [org,org,org,org,org,org,yel,yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr], 
                        [org,org,org,org,org,yel,yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr], 
                        [org,org,org,org,yel,yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl], 
                        [org,org,org,yel,yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl], 
                        [org,org,yel,yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl], 
                        [org,yel,yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl], 
                        [yel,yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl], 
                        [yel,yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl,blu], 
                        [yel,yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl,blu,blu], 
                        [yel,yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl,blu,blu,blu], 
                        [yel,yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl,blu,blu,blu,blu], 
                        [yel,yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl,blu,blu,blu,blu,blu], 
                        [yel,gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl,blu,blu,blu,blu,blu,blu], 
                        [gre,gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl,blu,blu,blu,blu,blu,blu,pur], 
                        [gre,gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl,blu,blu,blu,blu,blu,blu,pur,pur], 
                        [gre,gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl,blu,blu,blu,blu,blu,blu,pur,pur,pur], 
                        [gre,gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl,blu,blu,blu,blu,blu,blu,pur,pur,pur,pur], 
                        [gre,gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl,blu,blu,blu,blu,blu,blu,pur,pur,pur,pur,pur], 
                        [gre,dgr,dgr,dgr,dgr,dgr,dgr,lbl,lbl,lbl,lbl,lbl,blu,blu,blu,blu,blu,blu,pur,pur,pur,pur,pur,pur]]

        # Common: one of 1-3
        # Rare: Two of 1-3
        # Epic: Three of 1-4
        # Legendary: All of 2-5
        self.accessories = ['crazyeye','hat','tattoo','sunglasses','crown']

        self.choose_tier(tier)


    def choose_tier(self,tier):

        if tier == 'common':
            self.b = self.b[0]

            if randint(0,1) == 0:
                self.e = self.e[0]
            else:
                self.e = self.e[1]

            #TODO:
            # choose accessories

        elif tier == 'rare':
            self.b = self.b[1]
            if randint(0,1) == 0:
                self.e = self.e[0]
            else:
                self.e = self.e[1]

        elif tier == 'epic':
            self.b = self.b[2]
            if randint(0,1) == 0:
                self.e = self.e[0]
            else:
                self.e = self.e[1]

        elif tier == 'legendary':
            self.b = self.b[3]
            if randint(0,1) == 0:
                self.e = self.e[0]
            else:
                self.e = self.e[1]

    def yes_or_no(self):

        return randint(0,1) == 0

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


