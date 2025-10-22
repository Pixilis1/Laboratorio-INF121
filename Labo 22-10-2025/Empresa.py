

class Empresa:
    def __init__(self, nom):
        self.nom=nom
        self.empleados=[]

    def contratar(self,empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nom} contratado en la empresa {self.nom}")

    def listar_empleados(self):
        print(f"Empleados de la empresa {self.nom}")
        if len(self.empleados)==0:
            print(f"Aun no hay empleados en la empresa")
        else:
            i=0
            for empleado in self.empleados:
                print(f"{i}.{empleado}")
                i+=1


class Empleado:
    def __init__(self,nom,puesto,cDir,dDir,nDir):
        self.nom=nom
        self.puesto=puesto
        self.direccion=Direccion(cDir,dDir,nDir)

    def __str__(self):
        return f"Nombre:{self.nom} Puesto:{self.puesto} \n Direccion:{self.direccion}"

class Direccion:
    def __init__(self,ciudad,direccion,numero):
        self.ciudad=ciudad
        self.direccion=direccion
        self.numero=numero

    def __str__(self):
        return f"Ciudad:{self.ciudad} Direccion:{self.direccion} Numero:{self.numero}"


class main:
    e1=Empleado("Axel","Junior","La Paz","Monoblock",69953348)
    e2 = Empleado("John", "Junior", "La Paz", "Obelisco", 69953348)
    e3 = Empleado("Esperanza", "Magister", "La Paz", "Prado", 69953348)
    empresa1=Empresa("Zzzz")
    empresa1.listar_empleados()

    empresa1.contratar(e1)
    empresa1.contratar(e2)
    empresa1.contratar(e3)
    empresa1.listar_empleados()