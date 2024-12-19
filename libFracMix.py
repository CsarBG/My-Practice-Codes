from libFraccion import Fraccion

class FracMix(Fraccion):

    def __init__(self,ent,num=0,den=1):
        self.ent=ent
        super().__init__(num,den)    
        self.simplifica()
        super().simplifica()

    def __str__(self):
        return str(self.ent) + super().__str__()

    def simplifica(self):
        if self.num > self.den:
            aux=self.num//self.den
            self.ent=self.ent+aux
            self.num-=(aux*self.den)
    
    def __add__(self, obj):
        r=self.toFraccion()+obj.toFraccion()
        x=FracMix(0,r.num,r.den)
        x.simplifica()
        return x
    
    def __sub__(self, obj):
        r=self.toFraccion()-obj.toFraccion()
        x=FracMix(0,r.num,r.den)
        x.simplifica()
        return x

    def __mul__(self, obj):
        r=self.toFraccion()*obj.toFraccion()
        x=FracMix(0,r.num,r.den)
        x.simplifica()
        return x
    
    def __truediv__(self, obj):
        r=self.toFraccion()/obj.toFraccion()
        x=FracMix(0,r.num,r.den)
        x.simplifica()
        return x

    def toFraccion(self):
        n, d = self.num, self.den
        if self.ent!=0:
            n=(self.ent*d)+n
        f=Fraccion(n,d)
        return f