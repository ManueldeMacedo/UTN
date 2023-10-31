import random
import string
import Archivo

class Curso():
    prox_cod=0

    def __init__(self, nombre: str):
        self.__nombre                   =nombre
        self.__codigo                   =self.prox_cod
        self.__contrasenia_matriculacion=self.generar_contrasenia()
        self.__archivos                 =[]
        Curso.prox_cod+=1

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre

    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @property
    def contrasenia_matriculacion(self) -> str:
        return self.__contrasenia_matriculacion
    
    @property
    def archivos(self) -> list:
        return self.__archivos
    
    @property
    def __str__(self) -> str:
        return f"Nombre del curso: {self.__nombre}"
    
    def nuevo_archivo(self, archivo: Archivo) -> None:
        self.__archivos.append(archivo)
    
    @classmethod
    def generar_contrasenia(cls) -> str:
        contrasenia = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(contrasenia) for i in range(7))