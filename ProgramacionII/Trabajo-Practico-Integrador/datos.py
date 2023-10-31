#ARCHIVO PARA LLENAR LOS DATOS DEL PROGRAMA
from Estudiante import * 
from Profesor import *
from Usuario import *
from Curso import *
from Archivo import *
from Carrera import *

cursos = [
    Curso("Ingles I"),
    Curso("Ingles II"),
    Curso("Laboratorio I"),
    Curso("Laboratorio II"),
    Curso("Programacion I"),
    Curso("Programacion II")
]

estudiantes = [
    Estudiante("Manuel", "De Macedo", "manuel.demacedo@example.com", "contrasenia1", 12345, 2020, "Tecnicatura Universitaria en Programación"),
    Estudiante("Luciano", "Brion", "luciano.brion@example.com", "contrasenia2", 54321, 2019, "Tecnicatura Universitaria en Programación"),
    Estudiante("Brian", "Gerez", "brian.gerez@example.com", "contrasenia3", 98765, 2022, "Tecnicatura Universitaria en Programación")
]

profesores = [
    Profesor("Profesor1", "Apellido1", "profesor1@example.com", "contrasenia1", "Licenciado en Informática", 2010),
    Profesor("Profesor2", "Apellido2", "profesor2@example.com", "contrasenia2", "Doctor en Matemáticas", 2015)
]

carreras = [
    Carrera("Ingenieria mecánica", 5),
    Carrera("Tecnicatura Universitaria en Programación", 2),
    Carrera("Medicina", 5),
]