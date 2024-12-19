#Se crea la clase padre
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color=color
        self.ruedas=ruedas
    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)

#Se crea la clase hija, que hereda el formato del padre, pero añade difrerencias
#Entre los parentesis de define el padre
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        #Con super() apuntamos a la clase padre, y después del punto indicamos a qué parte del padre nos referimos
        #En vez del super() podríamos poner el nombre de la clase padre, pero agregaríamos "self" al parentesis
        super().__init__(color, ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
        return super().__str__()+", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

def main():
    y=Coche('azul', 4, 120, 1500)
    print(y)

if __name__=='__main__':
    main()