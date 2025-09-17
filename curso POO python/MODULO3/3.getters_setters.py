#PARA OBTENER EL VALOR DE UN ATRIBUTO ENCAPSULADO
#USAMOS GET
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad  #CON EL (_) YA SE CONVIERTE EN UN ATRIBUTO PRIVADO

    def get__nombre(self):
        return self.__nombre
    def get__edad(self):
        return self.__edad

    def set__edad(self, new_age):
        self.__edad = new_age

juni = Persona("juni", 45)

nombre = juni.get__nombre()
edad = juni.get__edad()
print(nombre, edad)

juni.set__edad(80)

edad = juni.get__edad()
print(nombre, edad)

print(f"Mi nombre es {nombre} y mi edad {edad}")


#AHORA QUIERO CAMBIAR EL VALOR DEL ATRIBUTO EDAD
#PARA ESTO SE USA SET    