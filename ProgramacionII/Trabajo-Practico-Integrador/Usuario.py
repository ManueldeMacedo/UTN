from abc import ABC

class Usuario(ABC):
    emails_unicos = {}

    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.__nombre     =nombre
        self.__apellido   =apellido
        self.__email      =self.__validar_email(email)
        self.__contrasenia=contrasenia

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido) -> None:
        self.__apellido = nuevo_apellido
    
    @property
    def email(self):
        return self.__email
    
    @property
    def contrasenia(self):
        return self.__contrasenia
    
    @property
    def __str__(self) -> str:
        return f"{self.nombre} | {self.apellido} | {self.email}"
    
    def __validar_email(self, email):
        if email in Usuario.emails_unicos:
            raise ValueError("El correo electrónico ya está en uso.")
        Usuario.emails_unicos[email] = True
        return email
    
    def validar_credenciales(self, email_user, contrasenia_user):
          return self.__email == email_user and self.__contrasenia == contrasenia_user