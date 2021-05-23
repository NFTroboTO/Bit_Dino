from base_model import base_model


class dino_1(base_model):

    def __init__(self, seedID, tier):
        super().__init__(seedID,tier)

        b = self.b
        o = self.o
        s = self.s
        h = self.h
        w = self.w
        e = self.e
        d = self.d    

        self.dino = [[b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b],
                    [b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b],
                    [b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b],
                    [b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b],
                    [b,b,b,b,b,b,b,b,b,b,b,o,o,o,o,o,b,b,b,b,b,b,b,b],
                    [b,b,b,b,b,b,b,b,b,b,o,o,s,s,s,o,o,o,b,b,b,b,b,b],
                    [b,b,b,b,b,b,o,o,o,o,o,s,s,s,s,s,s,o,o,o,b,b,b,b],
                    [b,b,b,b,b,o,h,h,h,o,s,s,s,s,s,s,s,s,s,o,o,b,b,b],
                    [b,b,b,b,b,o,h,h,o,o,s,s,s,s,s,s,s,s,s,s,o,o,b,b],
                    [b,b,b,b,b,o,o,h,o,s,s,s,s,s,s,w,w,s,s,s,s,o,o,b],
                    [b,b,b,b,b,b,o,o,o,s,s,s,s,s,s,w,e,s,s,s,s,s,o,b],
                    [b,b,b,b,b,b,b,o,s,s,s,s,s,s,s,s,s,s,s,s,s,s,o,b],
                    [b,b,b,o,o,o,o,o,s,s,s,s,s,s,s,s,s,s,s,s,s,s,o,b],
                    [b,b,o,h,h,h,o,s,s,s,s,s,s,o,o,o,o,o,o,o,o,o,o,b],
                    [b,b,o,h,h,h,o,s,s,s,s,s,s,s,s,s,s,s,s,s,o,b,b,b],
                    [b,b,o,h,h,o,o,s,s,s,s,s,s,s,s,s,o,o,o,o,o,b,b,b],
                    [b,b,o,o,h,o,s,s,s,s,s,s,s,s,s,s,o,b,b,b,b,b,b,b],
                    [b,b,b,o,o,o,s,s,s,s,s,s,s,s,s,s,o,b,b,b,b,b,b,b],
                    [b,b,b,b,o,s,s,s,s,s,s,s,s,s,s,d,o,b,b,b,b,b,b,b],
                    [o,o,o,o,o,s,s,s,s,s,s,s,s,s,d,d,d,o,b,b,b,b,b,b],
                    [h,h,h,o,s,s,s,s,s,s,s,s,s,s,d,d,d,d,o,b,b,b,b,b],
                    [h,h,o,s,s,s,s,s,s,s,s,s,s,d,d,d,d,d,d,o,b,b,b,b],
                    [h,o,s,s,s,s,s,s,s,s,s,s,d,d,d,d,d,d,d,d,o,b,b,b],
                    [o,o,s,s,s,s,s,s,s,s,s,d,d,d,d,d,d,d,d,d,d,o,b,b]]

class dino_2(base_model):

    def __init__(self, seedID):
        super().__init__(seedID)

        b = self.b
        o = self.o
        s = self.s
        h = self.h
        w = self.w
        e = self.e
        d = self.d
        t = self.t   

        self.dino =   [[b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b],
                        [b,b,b,b,b,b,b,b,b,h,h,h,b,b,b,b,b,b,b,b,b,b,b,b],
                        [b,b,b,b,b,b,b,b,h,h,h,h,h,b,b,b,b,b,b,b,b,b,b,b],
                        [b,b,b,b,b,b,b,h,h,h,h,h,h,h,b,b,b,b,b,b,b,b,b,b],
                        [b,b,b,b,b,b,o,o,o,o,o,o,o,o,b,b,b,b,b,b,b,b,b,b],
                        [b,b,b,b,o,o,o,s,s,s,s,s,s,o,o,b,b,b,b,b,b,b,b,b],
                        [b,b,b,o,o,s,s,s,s,s,s,s,s,s,o,o,b,b,b,b,b,b,b,b],
                        [b,b,b,o,s,s,s,s,s,s,s,s,s,s,s,o,b,b,b,b,b,b,b,b],
                        [b,b,o,o,s,s,s,e,s,s,s,s,e,s,s,o,o,b,b,b,b,b,b,b],
                        [b,b,o,s,s,s,e,e,e,s,s,e,e,e,s,s,o,o,b,b,b,b,b,b],
                        [b,b,o,s,s,s,s,e,s,s,s,s,e,s,s,s,s,o,o,b,b,b,b,b],
                        [b,b,o,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,o,o,o,b,b,b],
                        [b,b,o,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,o,o,b,b],
                        [b,b,o,o,s,s,s,s,s,s,s,s,o,s,s,s,s,o,s,o,s,o,b,b],
                        [b,b,b,o,s,s,s,s,s,s,s,s,t,o,s,s,s,s,s,s,s,o,b,b],
                        [b,b,b,o,s,s,s,s,s,s,s,s,t,t,o,o,s,s,s,s,s,o,b,b],
                        [b,b,b,o,o,s,s,s,s,s,s,s,s,t,s,o,o,o,o,o,o,o,b,b],
                        [b,b,b,b,o,o,s,s,s,s,s,s,s,s,s,o,o,o,o,o,b,b,b,b],
                        [b,b,b,b,b,o,s,s,s,s,s,s,s,s,s,o,b,b,b,b,b,b,b,b],
                        [b,b,b,b,o,o,s,s,s,s,s,s,s,s,o,o,b,o,o,o,o,o,b,b],
                        [b,b,b,o,o,s,s,s,d,d,d,s,s,s,o,o,o,o,o,o,o,o,b,b],
                        [b,b,b,o,s,s,s,s,d,d,d,s,s,s,s,o,o,o,o,o,b,o,b,b],
                        [b,b,o,o,s,s,s,d,d,d,d,d,s,s,s,s,o,b,b,o,b,b,b,b],
                        [b,b,o,s,s,s,d,d,d,d,d,d,d,s,s,s,o,o,b,b,b,b,b,b]]

class dino_3(base_model):

    def __init__(self, seedID):
        super().__init__(seedID)

        b = self.b
        o = self.o
        s = self.s
        w = self.w
        e = self.e
        p = (255,153,153)   

        self.dino = [[b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b], 
                     [b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b], 
                     [b,b,b,b,b,b,b,b,b,b,b,b,o,o,o,o,o,b,b,b,b,b,b,b], 
                     [b,b,b,b,b,b,b,b,b,b,b,o,s,s,s,s,s,o,o,o,b,b,b,b], 
                     [b,b,b,b,b,b,b,b,o,o,o,o,s,s,s,s,s,s,s,o,o,b,b,b], 
                     [b,b,b,b,b,o,o,o,o,s,s,s,s,s,s,s,s,o,o,s,o,b,b,b], 
                     [b,b,b,b,o,o,s,s,s,s,o,o,s,s,s,s,s,s,o,s,o,o,b,b], 
                     [b,b,b,b,o,s,s,s,o,o,o,o,o,s,s,s,s,s,s,s,s,o,b,b], 
                     [b,b,b,o,o,s,s,s,s,o,e,o,s,s,s,s,s,s,s,o,o,o,b,b], 
                     [b,b,b,o,s,s,s,s,s,o,w,o,s,s,s,s,s,s,o,o,w,b,b,b], 
                     [b,b,o,s,s,s,s,s,s,s,o,o,s,s,s,s,s,o,o,w,w,b,b,b], 
                     [b,o,o,s,s,s,s,s,s,s,s,s,s,s,s,s,o,o,w,b,w,b,w,b], 
                     [b,o,s,s,s,s,s,s,s,s,s,s,s,s,s,o,o,w,w,b,b,w,w,b], 
                     [o,o,s,s,s,s,s,s,s,s,s,s,s,o,o,o,w,b,w,b,w,o,o,b], 
                     [o,s,s,s,s,s,s,s,s,s,s,s,s,o,w,w,w,b,b,w,o,s,o,o], 
                     [s,s,s,s,s,s,s,s,s,s,s,s,s,o,p,w,b,b,w,o,o,s,s,o], 
                     [s,s,s,s,s,s,s,s,s,s,s,s,s,o,p,p,p,w,o,o,s,s,s,o], 
                     [s,s,s,s,s,s,s,s,s,s,s,s,s,o,o,o,o,o,o,s,s,s,s,o], 
                     [s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,o,o], 
                     [s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,o,b], 
                     [s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,o,o,b], 
                     [s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,o,o,b,b], 
                     [s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,o,o,o,b,b,b], 
                     [s,s,s,s,s,s,s,s,s,s,s,s,s,s,o,o,o,o,o,b,b,b,b,b]]




class dino_4(base_model):

    def __init__(self, seedID):
        super().__init__(seedID)

        b = self.b
        o = self.o
        s = self.s
        h = self.h
        w = self.w
        e = self.e
        d = self.d
        p = (s[0]-10,s[1]-10,s[2]-10) 
        z = (d[0]-10,d[1]-10,d[2]-10) 

        self.dino =    [[b,b,b,b,b,b,b,b,b,b,b,w,w,b,b,b,b,b,b,b,b,b,b,b],
                        [b,b,b,b,b,b,b,b,b,o,w,w,w,w,o,b,b,b,b,b,b,b,b,b],
                        [b,b,b,b,b,b,o,o,o,p,p,w,w,p,p,o,o,o,b,b,b,b,b,b],
                        [b,b,b,b,b,o,p,p,p,s,p,w,w,p,s,p,p,p,o,b,b,b,b,b],
                        [b,b,b,b,b,o,o,p,p,p,p,p,p,p,p,p,p,o,o,b,b,b,b,b],
                        [b,b,b,b,b,o,o,p,p,p,p,p,p,p,p,p,p,o,o,b,b,b,b,b],
                        [b,b,b,b,o,o,s,p,p,p,p,p,p,p,p,p,p,s,o,o,b,b,b,b],
                        [b,b,b,b,o,o,s,s,p,p,p,p,p,p,p,p,s,s,o,o,b,b,b,b],
                        [b,b,b,b,b,o,s,e,w,p,e,p,p,e,p,w,e,s,o,b,b,b,b,b],
                        [b,b,b,b,b,o,s,e,w,o,e,p,p,e,o,w,e,s,o,b,b,b,b,b],
                        [b,b,b,o,o,p,o,s,p,p,p,p,p,p,p,p,s,o,s,o,o,b,b,b],
                        [b,b,b,o,p,p,o,s,s,p,p,p,p,p,p,s,s,o,p,p,o,b,b,b],
                        [b,b,o,p,p,p,s,o,s,s,o,s,s,o,s,s,o,s,p,p,p,o,b,b],
                        [b,b,o,p,p,p,s,d,o,o,z,z,z,z,o,o,d,s,s,p,p,s,o,b],
                        [b,o,s,p,p,s,s,d,z,d,o,o,o,o,d,z,d,s,o,s,s,w,o,b],
                        [b,o,w,s,s,o,d,z,z,z,z,z,z,z,z,z,z,d,o,w,o,o,b,b],
                        [b,b,o,o,w,o,o,d,d,z,z,z,z,z,z,z,z,o,s,o,o,b,b,b],
                        [b,b,b,o,o,p,p,d,d,z,z,z,z,z,z,d,d,d,p,o,b,b,b,b],
                        [b,b,b,o,p,p,p,d,d,d,d,d,d,d,d,d,d,p,p,p,o,b,b,b],
                        [b,b,b,o,s,p,p,s,o,d,d,d,d,d,d,d,s,p,p,p,o,b,b,b],
                        [b,b,b,b,o,s,s,s,o,o,d,d,d,d,o,s,s,p,p,s,o,b,b,b],
                        [b,b,b,b,o,w,w,s,o,b,o,o,o,o,o,s,s,s,s,o,b,b,b,b],
                        [b,b,b,b,b,o,o,o,b,b,b,b,b,b,b,o,s,w,w,o,b,b,b,b],
                        [b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,o,o,o,b,b,b,b,b]]
