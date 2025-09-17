from abc import ABC, abstractmethod

# Clase abstracta
class Persona(ABC):
    def __init__(self, nombre, edad, sexo, trabajo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.trabajo = trabajo

    @abstractmethod
    def trabajar(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")

# Clase hija que implementa el método abstracto
class Programador(Persona):
    def trabajar(self):
        print(f"{self.nombre} está programando aplicaciones.")

# Crear instancia y usar los métodos
Usuario = Programador("Rucas", 21, "Masculino", "Programador")
Usuario.presentarse()
Usuario.trabajar()

