import random
import string

class Curso():
    def __init__(self, nombre:str):
        self.__nombre                    =nombre
        self.__contrasenia_matriculacion =self.generar_contrasenia()

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion

    def generar_contrasenia(self)->str:
        contrasenia = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(contrasenia) for i in range(7))