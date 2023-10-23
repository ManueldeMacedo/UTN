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
    email=input("Ingrese su email: ")

    for estudiante in estudiantes:
        if estudiante.email == email:
            bandera=1
            contrasenia = input("Ingrese su contraseña: ")
            if estudiante.contrasenia == contrasenia:
                print(f'Bienvenido/a {estudiante.nombre}')
                menu_alumno(estudiante)
                break
            else:
                print("Error de ingreso. Contraseña inválida.")
            
    if bandera==0:
        print("Correo electrónico no encontrado. Debe darse de alta en alumnado.")


def menu_alumno(estudiante):
    while True:
        print("\nMenú de Alumno:")
        print("1. Matricularse a un curso")
        print("2. Desmatricularse a un curso")
        print("3. Ver cursos")
        print("4. Volver al menú principal")

        opt = input("\nIngrese la opción de menú: ")
        if opt.isnumeric():
            if int(opt) == 1:
                matricular_alumno(estudiante)
            elif int(opt) == 2:
                desmatricular_alumno(estudiante)
            elif int(opt) == 3:
                cursos_alumno(estudiante)
            elif int(opt) == 4:
                print("Saliendo del menú de alumno...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Ingrese una opción numérica")


def matricular_alumno(estudiante):
    while True:
        cursos_ordenados = sorted(cursos, key=lambda curso: curso.nombre)
        for indice, curso in enumerate(cursos_ordenados, 1):
            print(f"{indice} {curso.nombre}")

        opt = input("\nIngrese el curso: ")
        if opt.isnumeric():
            opt=int(opt)
            if opt<=len(cursos):
                if cursos_ordenados[opt-1].nombre in estudiante.cursos:
                    print(f"Ya estás matriculado en {cursos_ordenados[opt-1].nombre}.")
                else:
                    contrasenia = input(f"Ingrese contraseña para matricularse: ")
                    
                    if contrasenia == cursos_ordenados[opt-1].contrasenia_matriculacion:
                        estudiante.cursos.append(cursos_ordenados[opt-1].nombre)
                        print("Se ha registrado correctamente su matriculación")
                    else:
                        print("Contraseña incorrecta")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Ingrese una opción numérica")


def desmatricular_alumno(estudiante):
    if len(estudiante.cursos)==0:
        print("Todavía no posee cursos matriculados.")
        return
    
    while True:
        for indice, curso in enumerate(estudiante.cursos, 1):
            print(f"{indice} {curso}")

        opt = input("\nIngrese el curso: ")
        if opt.isnumeric():
            opt=int(opt)
            if opt<=len(cursos):
                estudiante.cursos.remove(estudiante.cursos[opt-1])
                print("Se ha registrado correctamente su desmatriculación")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Ingrese una opción numérica")


def cursos_alumno(estudiante):
    if len(estudiante.cursos)==0:
        print("Todavía no posee cursos matriculados.")
        return
    
    while True:
        for indice, curso in enumerate(estudiante.cursos, 1):
            print(f"{indice} {curso}")

        opt = input("\nIngrese el curso: ")
        if opt.isnumeric():
            opt=int(opt)
            if opt<=len(estudiante.cursos):
                print(f"Nombre: {estudiante.cursos[opt-1]}")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Ingrese una opción numérica")


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
    cursos_ordenados = sorted(cursos, key=lambda curso: curso.nombre)
    print("Cursos disponibles:")
    for curso in cursos_ordenados:
        materia = f"Materia: {curso.nombre}"
        carrera = f"Carrera: Tecnicatura Universitaria en Programación"
        espacio_en_blanco = 20 - len(curso.nombre)
        print(f"{materia}{espacio_en_blanco * ' '}{carrera}")


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