class Persona:
    def __init__(self, nombre, edad): #__init__ es metodo contructor, Inicializa un objeto
        self.nombre = nombre
        self.edad = edad
        self.amigos = []  # Lista de amigos para usar con len()

    def agregar_amigo(self, amigo):  # Método extra para agregar amigos
        self.amigos.append(amigo)

    def __len__(self):
        # Devuelve la cantidad de amigos que tiene la persona
        return len(self.amigos)

class Usuario1(Persona):
    def __str__(self): #nos devuelve una representacion de una cadena de texto
        return f"Mi nombre es: {self.nombre} y mi edad es: {self.edad}"

class Usuario2(Persona): 
    def __repr__(self): #se usa si estás desarrollando una clase que:
        #se usará en debugging, forma parte de estructuras grandes (listas, diccionarios),
        # quieres que se pueda "recrear" copiando el texto
        return f"Persona('{self.nombre}', {self.edad})"
    #SIN EMBARGO SE PUEDE USAR SOLO __STR__


    
usuario = Usuario1("Dantes", 55)
usuario1 = Usuario2("Dantes", 55)
# Usamos el método agregar_amigo()
usuario.agregar_amigo("Carlos")
usuario.agregar_amigo("Lucía")

# Mostramos info
print(usuario)             # Llama a __str__
print(repr(usuario1))      # Llama a __repr__
print(len(usuario))        # Llama a __len__, muestra: 2