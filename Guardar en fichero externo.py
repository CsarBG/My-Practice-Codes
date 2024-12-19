import pickle

class persona():

    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print('Se ha creado una persona con el nombre de ', self.nombre)

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.genero, self.edad)

class listaPersonas():

    personas=[]

    def __init__(self):
        lista=open('Fichero.txt', 'ab+')
        lista.seek(0)
        try:
            self.personas=pickle.load(lista)
            print('Se cargarón {} personas del fichero'.format(len(self.personas)))
        except:
            print('Fichero vacio')
        finally:
            lista.close()
            del(lista)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonas()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p) 
    
    def guardarPersonas(self):
        lista=open('Fichero.txt', 'wb')
        pickle.dump(self.personas,lista)
        lista.close()
        del(lista)

    def mostrarFichero(self):
        print('La información del fichero es la siguiente:')
        for p in self.personas:
            print(p)

miLista=listaPersonas()
p=persona('Ana', 'Femenino', 19)
miLista.agregarPersonas(p)
miLista.mostrarFichero()