
class Persona:
    def __init__(self, nombre, paterno, materno, ci, edad):
        self._nombre = nombre
        self._paterno = paterno
        self._materno = materno
        self._ci = ci
        self._edad = edad

    def __str__(self):
        return f"nombre:{self._nombre}, paterno:{self._paterno}, materno:{self._materno}, ci:{self._ci}, edad:{self._edad}"

class Estudiante(Persona):
    def __init__(self, nombre, paterno, materno, ci, edad, ru, matricula):
        super().__init__(nombre, paterno, materno, ci, edad)
        self.__ru = ru
        self.__matricula  = matricula

    def getMatricula(self):
        return self.__matricula

    def __str__(self):
        return f"{super().__str__()}, regustroU:{self.__ru}, matricula{self.__matricula}"

class Rector(Persona):
    def __init__(self, nombre, paterno, materno, ci, edad, anios, sueldo):
        super().__init__(nombre, paterno, materno, ci, edad)
        self.__anios = anios
        self.__sueldo = sueldo

    def __str__(self):
        return f"{super().__str__()}, anios: {self.__anios}, sueldo:{self.__sueldo}"

class Carrera:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.estudiantes = []

    def agregaEstudiante(self, e :Estudiante):
        self.estudiantes.append(e)

    def __str__(self):
        cad = f"NOMBRE CARRERA:{self.__nombre}, estudiantes:\n"
        for e in self.estudiantes:
            cad = cad+ e.__str__() +"\n"
        return cad

    def cantEstudiantes(self):
        return len(self.estudiantes)

    def getEstudiantes(self):
        return self.estudiantes

    def getNombre(self):
        return self.__nombre

    '''def buscar(self, x:int):
        for e in self.estudiantes:
            if(e.getMatricula() == x):
                return e
        return False
    '''


class Facultad:
    def __init__(self, nombre, num):
        self.__nombre = nombre
        self.__nroCarreras = num
        self.__carreras = []

    def agregaCarrera(self, c: Carrera):
        self.__carreras.append(c)
        self.__nroCarreras = self.__nroCarreras + 1

    def __str__(self):
        cad = f"nombreFac:{self.__nombre}, numeroCarreras:{self.__nroCarreras}\n"
        for c in self.__carreras:
            cad = cad + c.__str__()
        return cad

    def getCarreras(self):
        return self.__carreras

    # def buscar(self, x:int):
    # for c in self.__carreras:
    # if(c.bucar(x)):

    def cantEstudiantes(self):
        contador = 0
        for c in self.__carreras:
            contador = contador + c.cantEstudiantes()
        return contador


class Universidad:
    def __init__(self, nombre, direccion, nombreRec, paterno, materno, ci, edad, anios, sueldo):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__rector = Rector(nombreRec, paterno, materno, ci, edad, anios, sueldo)
        self.__facultades = []

    def agregaFacultad(self, facu: Facultad):
        self.__facultades.append(facu)

    def __str__(self):
        cad = f"nombre:{self.__nombre}, direccion:{self.__direccion}, rector:{self.__rector}\n"
        for f in self.__facultades:
            cad = cad + f.__str__()
        return cad

    def cantEstudiantes(self):
        contador = 0
        for c in self.__facultades:
            contador = contador + c.cantEstudiantes()
        return contador

    def buscar(self, x: int):
        for f in self.__facultades:
            for c in f.getCarreras():
                for e in c.getEstudiantes():
                    if (e.getMatricula() == x):
                        return e

    def cambiarCarrera(self, matriculaEst: int, nombreCarreraNueva: str):
        estudianteAmover = None
        carreraActual = None
        carreraNuevaObj = None

        for f in self.__facultades:
            for c in f.getCarreras():
                for e in c.getEstudiantes():
                    if e.getMatricula() == matriculaEst:
                        estudianteAmover = e
                        carreraActual = c
                # también buscamos la carrera destino
                if c.getNombre().lower() == nombreCarreraNueva.lower():
                    carreraNuevaObj = c

        if estudianteAmover is None:
            print("No se encontró ningún estudiante con esa matrícula.")
            return
        if carreraNuevaObj is None:
            print("No se encontró la carrera destino.")
            return
        carreraActual.getEstudiantes().remove(estudianteAmover)
        carreraNuevaObj.agregaEstudiante(estudianteAmover)
        print(f"✅ El estudiante {estudianteAmover._nombre} fue cambiado a la carrera {carreraNuevaObj.getNombre()}.")


class Main():
    es1 = Estudiante("joel", "mollericona", "paco", 12935804, 18, 1886020, 4444)
    es2 = Estudiante("Axel", "quispe", "alvarez", 14913647, 23, 1881865671, 6020)
    es3 = Estudiante("luis", "sanchez", "lima", 12935804, 18, 1886020, 1234)
    es4 = Estudiante("maria", "galindo", "pa", 123455, 23, 444444, 6010)
    # print(es1, es2)
    c1 = Carrera("informatica")
    c2 = Carrera("Matematica")
    c2.agregaEstudiante(es3)
    c2.agregaEstudiante(es4)
    c1.agregaEstudiante(es1)
    c1.agregaEstudiante(es2)
    # print(c1)
    f1 = Facultad("ciencias puras", 0)
    f1.agregaCarrera(c1)
    f1.agregaCarrera(c2)
    f2 = Facultad("ingenieria", 0)
    # print(f1)
    u1 = Universidad("umsa", "la paz", "juab", "perez", "gutierrez", 1234, 40, 5, 24000)
    u1.agregaFacultad(f1)
    print("cantidad de estuiantes = ", u1.cantEstudiantes())
    print(u1.buscar(876))

    u1.cambiarCarrera(6020, "Matematica")
    print(u1)