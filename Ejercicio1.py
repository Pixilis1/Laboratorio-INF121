#Definir las clases Ram, computadora y discoDuro

class Ram:
    def __init__(self,capacidad,marca,tipo):
        self.__capacidad=capacidad
        self.__marca = marca
        self.__tipo = tipo


    def getCapacidad(self):
        return self.__capacidad

    def getMarca(self):
        return self.__marca

    def getTipo(self):
        return self.__tipo

    def mostrar(self):
        print(f"Capacidad:{self.__capacidad} Marca:{self.__marca} Tipo:{self.__tipo}")


class Computadora:
    def __init__(self,anioEnsamblaje,ram,discoDuro):
        self.__anioEnsamblaje=anioEnsamblaje
        self.__ram=ram
        self.__discoDuro=discoDuro
        self.__encendida = False

    def getAnioEnsamblaje(self):
        return self.__anioEnsamblaje

    def getRam(self):
        return self.__ram

    def getDiscoDuro(self):
        return self.__discoDuro

    def getEncendida(self):
        return self.__encedida

    def Encender(self):
        self.__encendida=True
        print("La pc esta encendida")

    def mostrar(self):
        print(f"Año de ensamblaje:{self.__anioEnsamblaje}")
        print(f"RAM Capacidad:{self.getRam().getCapacidad()} Marca:{self.getRam().getMarca()}\n"
              f"Disco Duro  Capacidad:{self.getDiscoDuro().getCapacidad()} Marca:{self.getDiscoDuro().getMarca()}")

    def modificarCapacidad(self):


class DiscoDuro:
    def __init__(self,capacidad,marca,modelo):
        self.__capacidad=capacidad
        self.__marca = marca
        self.__modelo = modelo

    def getCapacidad(self):
        return self.__capacidad

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

#a)Instanciar 3 computadoras de formas distintas
class Main:
    comp1=Computadora(2025)
    comp2=Computadora(2010)
    comp3 = Computadora(2020)




