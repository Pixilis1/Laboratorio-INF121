
#Sobre carga de metodos
from multipledispatch import dispatch

class Persona:
    def __init__(self,nom="Juan",edad=21):
        self.nom=nom
        self.edad=edad
    @dispatch()
    def mostrar(self):
        print(f"Nombre:{self.nom}\nEdad:{self.edad}")
    @dispatch(str)
    def mostrar(self,prof):
        print(f"Hola soy {self.nom} y trabajo de {prof}")

    @dispatch(str,int)
    def mostrar(self,prof, ci):
        print(f"Hola soy {self.nom}, trabajo de {prof} y mi carnet es {ci}")

    @dispatch(objet)
    def mostrar(self, otro):
        print(f"Hola soy {self.nom} y mi amigo es {otro}")


p=Persona()
p1=Persona("Axel",26)
p.mostrar(p1)
