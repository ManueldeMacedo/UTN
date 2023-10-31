from Curso import *

class Carrera():
    def __init__(self, nombre: str, cant_anios: int) -> None:
        self.__nombre     =nombre
        self.__cant_anios =cant_anios
        self.__cursos     =[]
        self.__estudiantes=[]

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def cant_anios(self) -> int:
        return self.__cant_anios
    
    @property
    def cursos(self) -> list:
        return self.__cursos
    
    @property
    def estudiantes(self):
        return self.__estudiantes
    
    @property
    def get_cantidad_materias(self) -> int:
        return None
    
    @property
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Cantidad de años : {self.cant_anios}, Estudiantes: {self.estudiantes}"