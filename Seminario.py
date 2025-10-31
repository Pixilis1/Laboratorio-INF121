

class Persona:



    #def leer(self):
     #   self.nom=input("Ingrese su name:")
      #  self.edad=input("Ingrese su edad:")

    #def mostrar(self):
     #   #print("Nombre:",self.nom)
      #  #print("Edad:", self.edad)
       # print(f"Nombre:{self.nom}\nEdad:{self.edad}")
        #print()
#p = Persona()
#p.leer()
#p.mostrar()
    def __init__(self,nom="Juan",edad=21):
        self.nom=nom
        self.edad=edad
    def mostrar(self):
        print(f"Nombre:{self.nom}\nEdad:{self.edad}")
    def __str__(self):
        return(f"Nombre:{self.nom}\nEdad:{self.edad}")
    def saludar(self,prof):
        print(f"Hola soy {self.nom} y trabajo de {prof}")
    def sumaEdad(self):
        return self.edad+10
    def mayorEdad(self,otro):
        if self.edad > otro.edad:
            print(f"{self.nom} es mayor")
        elif otro.edad > self.edad:
            print(f"{otro.nom} es mayor")
        else:
            print(f"Tienen la misma edad")
#Det si la p1 tendra la misma edad que la p2
    def mismaEdadCincoA(self,otro):
        a=self.edad+5
        if a==otro.edad:
            print("Tienen la misma edad dentro de 5 años")
        else:
            print("No tienen la misma edad dentro de 5 años")

p=Persona()
p1=Persona("Axel",26)
p.mostrar()
print(p1)
p1.saludar("Doctor")
print(p.sumaEdad())
p.mostrar()
p.mayorEdad(p1)

p.mismaEdadCincoA(p1)

