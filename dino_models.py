
'''
Create classes for each bit dino
The classes are inherited from the base model which picks the colors for different parts and accesories

TODO:
need to store the accessories info and return it to generate.py

'''


from base_model import base_model


class dino_1(base_model):

    def __init__(self, seedID, tier):
        super().__init__(seedID,tier)

    def get_dino(self):
        # base
        bb = (0,0,0)
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
        hh = self.h
        ee = self.e
        dd = self.d
        tt = self.t   

        # accessories

        dino =     [[bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,hh,hh,hh,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,hh,hh,hh,hh,hh,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,hh,hh,hh,hh,hh,hh,hh,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,oo,oo,oo,oo,oo,oo,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,oo,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,oo,oo,ss,ss,ss,ee,ss,ss,ss,ss,ee,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,ee,ee,ee,ss,ss,ee,ee,ee,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,ss,ee,ss,ss,ss,ss,ee,ss,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,oo,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb],
                    [bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,oo,ss,ss,ss,ss,oo,ss,oo,ss,oo,bb,bb],
                    [bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,tt,oo,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb],
                    [bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,tt,tt,oo,oo,ss,ss,ss,ss,ss,oo,bb,bb],
                    [bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,tt,ss,oo,oo,oo,oo,oo,oo,oo,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,oo,oo,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,oo,oo,oo,oo,oo,bb,bb],
                    [bb,bb,bb,oo,oo,ss,ss,ss,dd,dd,dd,ss,ss,ss,oo,oo,oo,oo,oo,oo,oo,oo,bb,bb],
                    [bb,bb,bb,oo,ss,ss,ss,ss,dd,dd,dd,ss,ss,ss,ss,oo,oo,oo,oo,oo,bb,oo,bb,bb],
                    [bb,bb,oo,oo,ss,ss,ss,dd,dd,dd,dd,dd,ss,ss,ss,ss,oo,bb,bb,oo,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,dd,dd,dd,dd,dd,dd,dd,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb]]

        return dino

    def get_mask(self):

        bb = 255

        oo = ss = hh = ee = dd = tt = 0

        # accessories

        mask =     [[bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,bb,hh,hh,hh,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,bb,hh,hh,hh,hh,hh,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,bb,hh,hh,hh,hh,hh,hh,hh,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,bb,oo,oo,oo,oo,oo,oo,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,oo,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,oo,oo,ss,ss,ss,ee,ss,ss,ss,ss,ee,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,ee,ee,ee,ss,ss,ee,ee,ee,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,ss,ee,ss,ss,ss,ss,ee,ss,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,oo,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb],
                    [bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,oo,ss,ss,ss,ss,oo,ss,oo,ss,oo,bb,bb],
                    [bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,tt,oo,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb],
                    [bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,tt,tt,oo,oo,ss,ss,ss,ss,ss,oo,bb,bb],
                    [bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,tt,ss,oo,oo,oo,oo,oo,oo,oo,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,oo,oo,oo,bb,bb,bb,bb],
                    [bb,bb,bb,bb,bb,oo,ss,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb,bb,bb,bb,bb,bb,bb,bb],
                    [bb,bb,bb,bb,oo,oo,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,oo,oo,oo,oo,oo,bb,bb],
                    [bb,bb,bb,oo,oo,ss,ss,ss,dd,dd,dd,ss,ss,ss,oo,oo,oo,oo,oo,oo,oo,oo,bb,bb],
                    [bb,bb,bb,oo,ss,ss,ss,ss,dd,dd,dd,ss,ss,ss,ss,oo,oo,oo,oo,oo,bb,oo,bb,bb],
                    [bb,bb,oo,oo,ss,ss,ss,dd,dd,dd,dd,dd,ss,ss,ss,ss,oo,bb,bb,oo,bb,bb,bb,bb],
                    [bb,bb,oo,ss,ss,ss,dd,dd,dd,dd,dd,dd,dd,ss,ss,ss,oo,oo,bb,bb,bb,bb,bb,bb]]  
                    
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
        
        gg = (255,153,153) # pink red

        # accessories

        #crazy eye
        crazyeye = self.yes_or_no()
        ee = self.e[crazyeye]

        # cry
        cs = [(102,178,255),ss] #[tear color, skin color]
        cry = self.yes_or_no()
        cs = cs[cry]

        # drool
        ls = [(153,204,255),ss]
        lo = [(102,178,255),oo]
        drool = self.yes_or_no()
        ls = ls[drool]
        lo = lo[drool]

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
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ls,lo,gg,gg,gg,ww,oo,oo,ss,ss,ss,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ls,lo,lo,oo,oo,oo,oo,ss,ss,ss,ss,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,ls,ls,ss,ss,ss,ss,ss,ss,ss,oo,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,ls,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ls,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ls,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ls,ss,ss,ss,ss,oo,oo,oo,bb,bb,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ls,oo,oo,oo,oo,oo,bb,bb,bb,bb,bb]]

        return dino
    

    def get_mask(self):
        # base
        bb = 255
        oo = ss = ww = ee = gg = cs = ls = lo =0

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
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ls,lo,gg,gg,gg,ww,oo,oo,ss,ss,ss,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ls,lo,lo,oo,oo,oo,oo,ss,ss,ss,ss,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,ls,ls,ss,ss,ss,ss,ss,ss,ss,oo,oo], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ss,ls,ss,ss,ss,ss,ss,ss,ss,ss,oo,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ls,ss,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,cs,ss,ss,ss,ls,ss,ss,ss,ss,ss,ss,ss,oo,oo,bb,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ls,ss,ss,ss,ss,oo,oo,oo,bb,bb,bb], 
                    [ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ls,oo,oo,oo,oo,oo,bb,bb,bb,bb,bb]]
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
        pp = (ss[0]-10,ss[1]-10,ss[2]-10) 
        zz = (dd[0]-10,dd[1]-10,dd[2]-10) 

        # accessories

        dino =     [[bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,ww,ww,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb,bb],
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

        return mask