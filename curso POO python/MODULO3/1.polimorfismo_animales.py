class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau 🐶")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau 🐱")

class Vaca(Animal):
    def hacer_sonido(self):
        print("Muuu 🐮")

# Función que usa polimorfismo
def reproducir_sonido(animal):
    animal.hacer_sonido()

# Lista de animales
animales = [Perro(), Gato(), Vaca()]

# Llamada en bucle
for a in animales:
    reproducir_sonido(a)