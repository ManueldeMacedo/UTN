from Usuario import *
from Curso import *
from Carrera import *

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo: int, anio_inscripcion_carrera: int, carrera: Carrera) -> None:
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo                  =legajo
        self.__anio_inscripcion_carrera=anio_inscripcion_carrera
        self.__carrera                 =carrera 
        self.__mis_cursos              =[]

    @property
    def legajo(self) -> int:
        return self.__legajo
    
    @legajo.setter
    def legajo(self, nuevo_legajo) -> None:
        self.__legajo = nuevo_legajo

    @property
    def anio_inscripcion_carrera(self) -> int:
        return self.__anio_inscripcion_carrera
    
    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, nuevo_anio_inscripcion_carrera) -> None:
        self.__anio_inscripcion_carrera = nuevo_anio_inscripcion_carrera

    @property
    def carrera(self):
        return self.__carrera     
    
    @property
    def mis_cursos(self) -> list:
        return self.__mis_cursos
    
    @property
    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido} - Legajo: {self.legajo} - Año de inscripción: {self.anio_inscripcion_carrera}"
    
    def matricular_en_curso(self, curso: Curso) -> None:
        self.__mis_cursos.append(curso)

    def desmatricular_en_curso(self, curso: Curso) -> None:
        self.__mis_cursos.remove(curso)