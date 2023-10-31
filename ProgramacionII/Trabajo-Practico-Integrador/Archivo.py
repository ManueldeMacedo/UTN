from datetime import date

class Archivo():
    variable_de_clase=0

    def __init__(self, nombre: str, formato: str):
        self.__nombre=nombre
        self.__fecha=date.today()
        self.__formato=formato

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre

    @property
    def fecha(self) -> str:
        return self.__fecha
    
    @fecha.setter
    def fecha(self, nuevo_fecha) -> None:
        self.__fecha = nuevo_fecha

    @property
    def formato(self) -> str:
        return self.__formato
    
    @formato.setter
    def formato(self, nuevo_formato) -> None:
        self.__formato = nuevo_formato

    @property
    def __str__(self) -> str:
        return f"Archivo: {self.nombre}{self.formato}"