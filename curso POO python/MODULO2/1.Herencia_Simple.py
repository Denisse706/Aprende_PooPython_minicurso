class Animal:
    def hablar(self):
        print("Hace un sonido")

class Perro(Animal):  # ✅ Solo una clase hija
    def hablar(self):
        print("Guau")

#LA CLASE HIJA PERRO HEREDA DE LA CLASE ANIMAL
perro = Perro()
perro.hablar()  # Muestra: Guau