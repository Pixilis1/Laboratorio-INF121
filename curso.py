
class Estudiante:
    def __init__(self, nombre, matricula):
        self.__nombre=nombre
        self.__matricula=matricula
    def __str__(self):
        return f"Nombre:{self.__nombre}, Matricula:{self.__matricula}"
class Curso:
    def __init__(self, nroEstudiantes):
        self.__nroEstudiantes=nroEstudiantes
        self.__estudiantes=[]
    def __str__(self):
        cad=f"Numero de estudiantes:{self.__nroEstudiantes}\n"
        for i in range(self.__nroEstudiantes):
            cad = cad + f"{self.__estudiantes[i].__str__()}\n"
        return cad
    def agregarEstudiante(self,e):
        self.__estudiantes.append(e)
        self.__nroEstudiantes=self.__nroEstudiantes+1

class Main():
    curso=Curso(0)
    estudiante1=Estudiante("Axel",14913647)
    curso.agregarEstudiante(estudiante1)
    print(curso)
    estudiante2=Estudiante("John",14913648)
    curso.agregarEstudiante(estudiante2)
    print(curso)
    estudiante3 = Estudiante("Jajas", 14913649)
    curso.agregarEstudiante(estudiante3)
    print(curso)
    