class Estudiante:
    def __init__(self, nombre, edad, grado): #__init__	Al crear un objeto. Para inicializar atributos automáticamente
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def __str__(self): #__str__	Al imprimir un objeto con print(obj). Para que se vea legible y descriptivo
        return f"Nombre: {self.nombre} |Edad: {self.edad} |Graddo: {self.grado}"
    
#BASE DE DATOS PRINCIPAL
base_datos_estudiantes = []

#REGISTRAR ESTUDIANTE
def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    grado = input("Ingrese el grado del estudiante: ")
    estudiante = Estudiante(nombre, edad, grado)
    base_datos_estudiantes.append(estudiante)
    print("Estudiante registrado con éxito")

#MOSTRAR ESTUDIANTES ALFABETICAMENTE
def mostrar_estudiante():
    if not base_datos_estudiantes:
        print("no hay estuddiantes registrados")
        return
    estudiantes_ordenados = sorted(base_datos_estudiantes, key= lambda est: est.nombre.lower())
    for idx, est in enumerate(estudiantes_ordenados):
        print(f"{idx + 1}. {est}")

#ELIMINAR ESTUDIANTE POR NUMERO
def eliminar_estudiante():
    mostrar_estudiante()
    try:
        numero = int(input("Ingrese el numero del estudiante a eliminar: ")) -1
        if 0 <= numero <len(base_datos_estudiantes):
            eliminando = base_datos_estudiantes.pop(numero)
            print(f"Estudiante eliminado: {eliminando.nombre}")
        else:
            print("Numero invalido")
        
    except ValueError:
        print("Entrada inválida, debe ser un numero")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Eliminar estudiante")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        mostrar_estudiante()
    elif opcion == "3":
        eliminar_estudiante()
    elif opcion == "4":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción inválida.")