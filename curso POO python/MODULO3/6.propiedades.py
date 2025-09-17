class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self._edad 

    @nombre.setter
    def nombre(self, new_name):
        self.__nombre = new_name
    
    @edad.deleter
    def edad (self):
        del self._edad

Usuario = Persona("Rafael", 59)

nombre = Usuario.nombre
edad = Usuario.edad

print(nombre,edad)

del Usuario.edad

Usuario.nombre = "Randalf"

nombre = Usuario.nombre
print(nombre)
