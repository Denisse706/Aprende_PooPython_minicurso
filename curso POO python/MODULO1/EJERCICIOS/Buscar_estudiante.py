#-Crear una clase Estudiante para modelar los datos de un estudiante.
#-Pedir al usuario que ingrese esos datos.
#-Guardar cada estudiante en una lista (como base de datos temporal).
#-Repetir el proceso si se quiere agregar más estudiantes.
#-Mostrar todos los estudiantes registrados.

class Estudiante:
    def __init__(self):
        self.nombre = input("INGRESA TU NOMBRE: ")
        self.edad = input("INGRESA TU EDAD: ")
        self.grado = input("INGRESA TU GRADO: ")
    
    def mostrar_info(self):
        print(f"NOMBRE: {self.nombre}, EDAD: {self.edad}, GRADO: {self.grado}")

#LISTA PARA ALMACENAR ESTUDIANTES (SIMULANDO BASE DE DATOS)
base_datos_estudiantes = [] #Es simplemente una lista vacía. Cada vez que registremos un estudiante, lo agregaremos aquí.

#CREAR VARIOS ESTUDIANTES
while True:
    nuevo_estudiante = Estudiante() #Creamos un nuevo objeto de la clase Estudiante, lo cual activa el input() para llenar los datos
    base_datos_estudiantes.append(nuevo_estudiante) #Lo agregamos a la lista con .append()
    
    continuar = input("¿Deseas registrar a otro estudiante? (s/n): ").lower()
    if continuar != "si":
        break

#ORDENAR ALFABETICAMENTE
base_datos_estudiantes.sort(key=lambda estudiante: Estudiante.nombre)

for i, est in enumerate(base_datos_estudiantes):
    print(f"{i + 1}. {est.nombre}")# Índice visible empieza en 1

#BUSQUEDA POR NUMEROS Y CARACTERISTICA
while True:
    try:
        numero = int(input("\nIngrese el numero del estudiante que desee consultar:"))-1
        if numero < 0 or numero >= len(base_datos_estudiantes):
            print("numero fuera de rango. Intente de nuevo")
            continue
        caracteristicas = input("¿Que deseas ver? (nombre, edad, grado): ").strip().lowwer()

        estudiante = base_datos_estudiantes[numero]
       
        if hasattr(estudiante, caracteristicas):
            print(f"{caracteristicas.capitalize()} del estudiante {numero + 1}: {getattr(estudiante, caracteristicas)}")
        else:
            print("Caracteristica no validad, intente de nuevo con: nombre, edad, grado.")
       
        continuar = input("¿Deseas consultar otro estudiante? (s/n)").lower()
        if continuar != "si":
            break
    except ValueError:
        print("entrada invalidad, debe ingresar nuevamente un numero")