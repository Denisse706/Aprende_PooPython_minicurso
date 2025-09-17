class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    # METODOS
    #TODAS LAS FUNCIONES QUE SE CREEN DENTRO DE UNA CLASE SON METODOS 
    #LA FUNCION DEL METODO ES DEFINIR LAS ACCIONES QUE PUEDE HACER EL OBJETO
    def llamar(self):
        print(f"Acabas de realizar una llamada desde un: {self.modelo}")

    def cortar(self):
        print(f"Acabas de finalizar una llamada desde un: {self.marca}")

# Creación correcta de objetos
Celular1 = Celular("Samsung", "S23", "48MP")
Celular2 = Celular("Apple", "Iphone 15 pro", "96MP")

Celular2.llamar()