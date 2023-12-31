from Estudiante import * 
from Profesor import *
from Usuario import *
from Curso import *
from Archivo import *
import datos

def validar_alumno():

    bandera=0
    email=input("Ingrese su email: ")

    for estudiante in datos.estudiantes:
        if estudiante.email == email:
            bandera=1
            contrasenia = input("Ingrese su contraseña: ")
            if estudiante.validar_credenciales(email, contrasenia):
                print(f'Bienvenido/a {estudiante.nombre}')
                menu_alumno(estudiante)
                break
            else:
                print("Error de ingreso. Contraseña inválida.")
            
    if bandera==0:
        print("Correo electrónico no encontrado. Debe darse de alta en alumnado.")


def menu_alumno(estudiante: Estudiante):
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


def matricular_alumno(estudiante : Estudiante):
    while True:
        cursos_ordenados = sorted(datos.cursos, key=lambda curso: curso.nombre)
        for indice, curso in enumerate(cursos_ordenados, 1):
            print(f"{indice} {curso.nombre}")

        opt = input("\nIngrese el curso: ")
        if opt.isnumeric():
            opt=int(opt)
            if opt<=len(datos.cursos):
                nombre_curso = cursos_ordenados[opt-1].nombre

                if esta_matriculado(estudiante, nombre_curso):
                    print(f"Ya estás matriculado en {nombre_curso}")
                else:
                    contrasenia = input(f"Ingrese contraseña para matricularse: ")
                    
                    if contrasenia == cursos_ordenados[opt-1].contrasenia_matriculacion:
                        estudiante.matricular_en_curso(cursos_ordenados[opt-1])
                        print("Se ha registrado correctamente su matriculación")
                    else:
                        print("Contraseña incorrecta")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Ingrese una opción numérica")


def desmatricular_alumno(estudiante : Estudiante):
    if len(estudiante.mis_cursos)==0:
        print("Todavía no posee cursos matriculados.")
        return
    
    while True:
        for indice, curso in enumerate(estudiante.mis_cursos, 1):
            print(f"{indice} {curso.nombre}")

        opt = input("\nIngrese el curso: ")
        if opt.isnumeric():
            opt=int(opt)
            if opt<=len(datos.cursos):
                estudiante.desmatricular_en_curso(estudiante.mis_cursos[opt-1])
                print("Se ha registrado correctamente su desmatriculación")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Ingrese una opción numérica")


def cursos_alumno(estudiante):
    if len(estudiante.mis_cursos)==0:
        print("Todavía no posee cursos matriculados.")
        return
    
    while True:
        for indice, curso in enumerate(estudiante.mis_cursos, 1):
            print(f"{indice} {curso.nombre}")

        opt = input("\nIngrese el curso: ")
        if opt.isnumeric():
            opt=int(opt)
            if opt<=len(estudiante.mis_cursos):
                print(f"Nombre: {estudiante.mis_cursos[opt-1].nombre}")
                archivos_ordenados = sorted(estudiante.mis_cursos[opt-1].archivos, key=lambda archivo: archivo.fecha)
                for archivo in archivos_ordenados:
                    print(archivo.__str__)
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Ingrese una opción numérica")



def validar_profesor():

    bandera=0    
    email = input("Ingrese su email: ")

    for profesor in datos.profesores:
        if profesor.email == email:
            bandera=1
            contrasenia = input("Ingrese su contraseña: ")
            if profesor.validar_credenciales(email, contrasenia):
                print(f'Bienvenido/a {profesor.nombre}')
                menu_profesor(profesor)
                break
            else:
                print("Error de ingreso. Contraseña inválida.")

    if bandera==0:
        print("Correo electrónico no encontrado")
        while True:
            opt = input("Ingrese código para registrarse: ")
            if opt.lower() == "admin":
                datos.profesores.append(Profesor.registrar(email))
                break
            
            else:
                print("Código Incorrecto, regresando al menu principal... ")
                break


def menu_profesor(profesor: Profesor):
    while True:
        print("\nMenú de Profesor:")
        print("1. Dictar un curso")
        print("2. Ver curso")
        print("3. Volver al menú principal")

        opt = input("\nIngrese la opción de menú: ")
        if opt.isnumeric():
            if int(opt) == 1:
                dictar_curso(profesor)
            elif int(opt) == 2:
                cursos_profesor(profesor)
            elif int(opt) == 3:
                print("Saliendo del menú de Profesor...")
                break
          
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Ingrese una opción numérica")

def dictar_curso(profesor: Profesor):
     while True:
        cursos_ordenados = sorted(datos.cursos, key=lambda curso: curso.nombre)
        for indice, curso in enumerate(cursos_ordenados, 1):
            print(f"{indice} {curso.nombre}")

        opt = input("\nIngrese el curso: ")
        if opt.isnumeric():
            opt=int(opt)
            if opt<=len(datos.cursos):
                nombre_curso = cursos_ordenados[opt-1].nombre
                if esta_matriculado(profesor, nombre_curso):
                    print(f"Ya estás matriculado en {nombre_curso}")
                else:
                    profesor.dictar_curso(cursos_ordenados[opt-1])
                    print("Se ha registrado correctamente su matriculación")
                    print(f"Nombre: {cursos_ordenados[opt-1].nombre}")
                    print(f"Código: {cursos_ordenados[opt-1].codigo}")
                    print(f"Contraseña: {cursos_ordenados[opt-1].contrasenia_matriculacion} ")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Ingrese una opción numérica")

def cursos_profesor(profesor: Profesor):
    
    if len(profesor.mis_cursos)==0:
        print("Todavía no posee cursos matriculados.")
        return
    
    while True:
        for indice, curso in enumerate(profesor.mis_cursos, 1):
            print(f"{indice} {curso.nombre}")

        opt = input("\nIngrese el curso: ")
        if opt.isnumeric():
            opt=int(opt)
            if opt<=len(profesor.mis_cursos):
                print(f"Nombre: {profesor.mis_cursos[opt-1].nombre}")
                print(f"Código: {profesor.mis_cursos[opt-1].codigo}")
                print(f"Contraseña: {profesor.mis_cursos[opt-1].contrasenia_matriculacion} ")
                print(f"Cantidad de archivos: {len(profesor.mis_cursos[opt-1].archivos)} ")

                files = input("\nDesea ingresar un nuevo archivo?: Si/No")
                if files.upper()=="SI":
                    file_name = input("\nIngrese el nombre del archivo: ")
                    file_format = input("\nIngrese el formato del archivo: ")
                    archivo_new=Archivo(file_name, file_format)
                    profesor.mis_cursos[opt-1].nuevo_archivo(archivo_new)
                    print("Su archivo fue cargado exitosamente.")

                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Ingrese una opción numérica")

    

def ver_cursos():
    cursos_ordenados = sorted(datos.cursos, key=lambda curso: curso.nombre)
    print("Cursos disponibles:")
    for curso in cursos_ordenados:
        materia = f"Materia: {curso.nombre}"
        carrera = f"Carrera: Tecnicatura Universitaria en Programación"
        espacio_en_blanco = 20 - len(curso.nombre)
        print(f"{materia}{espacio_en_blanco * ' '}{carrera}")

def esta_matriculado(estudiante, nombre_curso):
    return nombre_curso in [curso.nombre for curso in estudiante.mis_cursos]

def esta_matriculado(profesor, nombre_curso):
    return nombre_curso in [curso.nombre for curso in profesor.mis_cursos]


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