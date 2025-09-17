#MEJORA LA LEGIBILIDAD DEL CODIGO
#EL MANTENIMIENTO Y EVOLUCIÓN DEL CODIGO

#1. ATRIBUTO PRIVADO CON UN SOLO_
#A ESTOS SE PUEDE ACCEDER FACILMENTE
class Miclase:
    def __init__(self):
        self._atributo_privado = "valor" #SOLO HAY QUE AGREGAR _ LUEGO DE "self."
object = Miclase()
print (object._atributo_privado)



#2. ATRIBUTO MUY PRIVADO CON mangling (__)
#PARA ACCEDER A ESTOS HAY QUE UTILIZAR: GETTERS Y SETTERS
class Miclase:
    def __init__(self):
        self.__atributo_privado = "valor" #SOLO HAY QUE AGREGAR (2)__ LUEGO DE "self."

