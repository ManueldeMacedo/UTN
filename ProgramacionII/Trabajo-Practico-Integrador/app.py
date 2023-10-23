from Estudiante import * 
from Profesor import *
from Usuario import *
from Curso import *

cursos = [
    Curso("Ingles I"),
    Curso("Ingles II"),
    Curso("Laboratorio I"),
    Curso("Laboratorio II"),
    Curso("Programacion I"),
    Curso("Programacion II")
]

estudiantes = [
    Estudiante("Manuel", "De Macedo", "manuel.demacedo@example.com", "contrasenia1", "12345", 2020),
    Estudiante("Luciano", "Brion", "luciano.brion@example.com", "contrasenia2", "54321", 2019),
    Estudiante("Brian", "Gerez", "brian.gerez@example.com", "contrasenia3", "98765", 2022)
]

profesores = [
    Profesor("Profesor1", "Apellido1", "profesor1@example.com", "contrasenia1", "Licenciado en Informática", 2010),
    Profesor("Profesor2", "Apellido2", "profesor2@example.com", "contrasenia2", "Doctor en Matemáticas", 2015)
]

def validar_alumno():

    bandera=0    
    email = input("Ingrese su email: ")

    for estudiante in estudiantes:
        if estudiante.email == email:
            bandera=1
            contrasenia = input("Ingrese su contraseña: ")
            if estudiante.contrasenia == contrasenia:
                print(f'Bienvenido/a {estudiante.nombre}')
                break
            else:
                print("Error de ingreso. Contraseña inválida.")
            
    if bandera==0:
        print("Correo electrónico no encontrado. Debe darse de alta en alumnado.")

def validar_profesor():

    bandera=0    
    email = input("Ingrese su email: ")

    for profesor in profesores:
        if profesor.email == email:
            bandera=1
            contrasenia = input("Ingrese su contraseña: ")
            if profesor.contrasenia == contrasenia:
                print(f'Bienvenido/a {profesor.nombre}')
                break
            else:
                print("Error de ingreso. Contraseña inválida.")
            
    if bandera==0:
        print("Correo electrónico no encontrado. Debe darse de alta en alumnado.")

def ver_cursos():
    for curso in cursos:
        print(f"Nombre del curso: {curso.nombre} , Carrera: Tecnicatura universitaria en programacion")

def main_menu():
    while True:
        print("\nMenú de Usuario:")
        print("1. Ingresar como alumno")
        print("2. Ingresar como profesor")
        print("3. Ver cursos")
        print("4. Salir")

        opt = input("\nIngrese la opción de menú: ")
        if opt.isnumeric():
            if int(opt) == 1:
                validar_alumno()
            elif int(opt) == 2:
                validar_profesor()
            elif int(opt) == 3:
                ver_cursos()
            elif int(opt) == 4:
                print("Saliendo del menú...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Ingrese una opción numérica")

main_menu()