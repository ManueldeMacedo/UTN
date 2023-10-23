from Usuario import *

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera)->None:
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo                   =legajo
        self.__anio_inscripcion_carrera =anio_inscripcion_carrera
        self.__cursos                   =[]

    @property
    def legajo(self):
        return self.__legajo

    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    @property
    def cursos(self) -> list:
        return self.__cursos