# HERENCIA MULTIPLE

# Clase padre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return (f"Hola, soy {self.nombre}.")

# Clase hija 1
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return (f"Mi habilidad es: {self.habilidad}")
        
# Clase hija 2
class Empleadoartista(Persona,Artista):
    def __init__(self, nombre, edad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
   
    def presentarse(self):
        print (f'Hola mi nombre es {self.nombre}, tengo {self.edad} años, mi sueldo es de {self.salario} y trabajo en {self.empresa}')

Antonio = Empleadoartista("Antonio", 55, "vende", 10.000, "Macdonals")

#Antonio.presentarse()

herencia = issubclass(Empleadoartista, Artista) #la clase EmpleadoArtista es una subclase de la clase Artista [TRUE]
instancia = isinstance(Antonio, Persona) #El objeto Antonio es uns instancia de la clase Persona [TRUE] 
print(herencia, instancia)