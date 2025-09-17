class Robot:
    # __new__ se ejecuta antes que __init__. Se encarga de crear el objeto.
    # Es raro modificarlo, pero sirve si necesitas controlar la creación de la instancia, como en singletons o metaprogramación.
    def __new__(cls, nombre, modelo):
        print(f"🛠️ Creando un nuevo robot: {nombre} ({modelo})")
        instancia = super().__new__(cls)  # Aquí se crea el objeto
        return instancia

    # __init__ inicializa el objeto con los datos que le damos
    def __init__(self, nombre, modelo):
        print(f"🔧 Inicializando el robot {nombre}")
        self.nombre = nombre
        self.modelo = modelo

    # __repr__ devuelve cómo se ve el objeto cuando lo imprimes,
    def __repr__(self):
        return f"🤖 Robot(nombre='{self.nombre}', modelo='{self.modelo}')"
    # Cuando haces print(objeto), Python llama a este método.

    # __del__ se llama cuando el objeto es eliminado (normalmente al final del programa o con del)
    # No es muy usado salvo para liberar recursos.
    def __del__(self):
        print(f"💥 Eliminando el robot {self.nombre} ({self.modelo})")

# 🧪 Probamos la clase
print("== INICIO ==")
r1 = Robot("Tito", "A1")
print(r1)  # Se llama a __repr__

print("== Fin del programa ==")
del r1  # Esto llama a __del__, aunque puede ser automático al final
