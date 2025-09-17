class Celular():
#VAMOS A CREAR UN METODO ESPECIAL PARA QUE AL INSTANCIAR UNA CLASE SE EJECUTE AUTOMATICAMENTE
#CADA VES QUE SE CREA UN OBJETO SE EJECUTA LA SIGUIENTE ESTRUCTURA QUE SE LLAMA:
#FUNCION CONSTRUCTORA
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

Celular1 = Celular("Samsung", "S23", "48MP")
Celular2 = Celular("Apple", "Iphone 15 pro", "96MP") 
print(Celular2.marca)