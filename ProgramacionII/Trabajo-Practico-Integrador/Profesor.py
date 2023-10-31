from Usuario import *
from Curso import *

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo     =titulo
        self.__anio_egreso=anio
        self.__mis_cursos     =[]

    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo) -> None:
        self.__titulo = nuevo_titulo
    
    @property
    def anio_egreso(self) -> int:
        return self.__anio_egreso
    
    @anio_egreso.setter
    def anio_egreso(self, nuevo_anio_egreso) -> None:
        self.__anio_egreso = nuevo_anio_egreso
    
    @property
    def mis_cursos(self) -> list:
        return self.__mis_cursos
    
    def dictar_curso(self, curso: Curso):
        self.mis_cursos.append(curso)
    
    @property
    def __str__(self) -> str:
        return f"Profesor: {self.nombre} {self.apellido}, Email: {self.email}, Titulo: {self.titulo}, Anio Egreso: {self.anio_egreso}"
    
    @classmethod
    def registrar(cls, email_input):
        nombre      =input("Ingrese su nombre: ")
        apellido    =input("Ingrese apellido: ")
        contrasenia =input("Ingrese contrasenia: ")
        titulo      =input("Ingrese su título: ")
        anio        =int(input(f"Ingrese el año en que egresó de {titulo}: "))

        nuevo_profesor = Profesor(nombre,apellido,email_input,contrasenia,titulo,anio)

        return nuevo_profesor