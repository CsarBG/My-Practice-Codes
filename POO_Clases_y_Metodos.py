class fraccion:

#__init_ es el ciclo de iniciación de cualquier objeto que sea de está clase   
    def __init__(self, num=0, den=1):
        self.num=num
        self.den=den
#__del__ se usa para eliminar un objeto que no se esté usando, ni sea referenciado

#__mul__ sobre carga el operador "*" (solo sustituí "multiplica" por "__mul__")
    def __mul__(self,b):
        num=self.num*b.num
        den=self.den*b.den
        r=fraccion(num,den)
        return r
#Buscar por object overloading para ver otros metodos

    def simplificar(self):
        for i in range (10, 1, -1):
            if self.num%i==0 and self.den%i==0:
                self.num=int(self.num/i)
                self.den=int(self.den/i)
                self.simplificar()

    def imprime(self):
        print("[", self.num, "/", self.den, "]")

def main():
    a=fraccion(5,14)
    b=fraccion(14,25)
    a.imprime()
    b.imprime()
    c=a*b
    c.simplificar()
    c.imprime()
    

if __name__=="__main__":
    main()  

#issubclass([Clase que queremos checar], [Clase que creemos es el padre])
#isinstance([Objeto], [Clase de la que creemos que fue creeada]) 
#isinstance al revisarse con un objeto creado a partir de una subclase, la clase padre también dara True