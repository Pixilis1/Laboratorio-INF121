

class Persona:
    def __init__(self, nom, pat, mat, ci, edad):
        self.nom=nom
        self.pat=pat
        self.mat=mat
        self.ci=ci
        self.edad=edad


class Estudiante(Persona):
    def __init__(self,nom,pat,mat,ci,edad,ru,matricula,carrera):
        super().__init__(nom,pat,mat,ci,edad)
        self.ru=ru
        self.matricula=matricula
        self.carrera=carrera

class Rector(Persona):
    def __init__(self, nom,pat,mat,ci,edad,aniosExp,sueldo,universidad):
        super().__init__(nom,pat,mat,ci,edad)
        self.aniosExp=aniosExp
        self.sueldo=sueldo
        self.universidad=universidad

class Universidad:
    def __init__(self,nom,direccion,facultades):
        self.nom=nom
        self.direccion=direccion
        self.facultades=[]

    def agregarFacu(self,nom,nroCarreras):
        facultad=Facultad(nom,nroCarreras,self)
        self.facultades.append(facultad)

class Carrera:
    def __init__(self,nom):
        self.nom=nom
        self.estudiantes=[]

    def agregarEstudiante(self,estudiante):
        self.estudiantes.append(estudiante)

    def contarEstudiantes(self):
        return len(self.estudiantes)

class Facultad:
    def __init__(self,nom,nroCarreras):
        self.nom=nom
        self.nroCarreras=nroCarreras
        self.carreras=[]

    def agregarCarrera(self,nom):
        carrera=Carrera(nom,self)
        self.carreras.append(carrera)

uni1=Universidad("UMSA","Monoblock",2)
uni2=Universidad("SAN SIMON","COCHABAMBA",3)

facu1=Facultad("CPN")
facu2=Facultad("Ingenieria")
facu3=Facultad("Medicina")
uni1.agregarFacu(facu1)
uni1.agregarFacu(facu2)
uni1.agregarFacu(facu3)

carrera1=Carrera("Informatica")
facu1.agregarCarrera(carrera1)
carrera2=Carrera("Civil")
facu2.agregarCarrera(carrera2)
carrera3=Carrera("Laboratorio")
facu3.agregarCarrera(carrera3)

est1=Estudiante("Axel","Quispe","Alvarez",14913647,23,1865671,123456,"Informatica")
est2=Estudiante("John","Quispe","Alvarez",14913648,20,1865672,123456,"Civil")
est3=Estudiante("Arleth","Quispe","Alvarez",14913649,10,1865673,123456,"Laboratorio")
est4=Estudiante("Mihael","Quispe","Alvarez",14913647,23,1865671,123456,"Informatica")
est5=Estudiante("Michel","Quispe","Alvarez",14913648,20,1865672,123456,"Informatica")
est6=Estudiante("Lautaro","Quispe","Alvarez",14913649,10,1865673,123456,"Medicina")

carrera1.agregarEstudiante(est1)
carrera1.agregarEstudiante(est4)
carrera1.agregarEstudiante(est5)

