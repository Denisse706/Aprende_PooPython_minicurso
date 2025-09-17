# HERENCIA JERÁRQUICA

# Clase padre
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}.")

# Clase hija 1
class Estudiante(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad
        print(f"{self.nombre} está estudiando y tiene {self.edad} Años")

# Clase hija 2
class Profesor(Persona):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre)
        self.sueldo = sueldo
        print(f"{self.nombre} está enseñando y su sueldo es {self.sueldo}")

# Clase hija 3
class Director(Persona):
    def __init__(self, nombre, time):
        super().__init__(nombre)
        self.time = time
        print(f"{self.nombre} está dirigiendo la institución y lleva trabajando allí {self.time} años")

# Pruebas visuales
print("\n== HERENCIA JERÁRQUICA ==")
persona1 = Estudiante("Carlos", 18)
persona2 = Profesor("Lucía", 40000)
persona3 = Director("Martín", 8)


