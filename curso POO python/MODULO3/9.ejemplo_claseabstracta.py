from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

firulais = Perro("Firulais")
firulais.hablar()