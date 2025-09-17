class Pocion:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder  # número entero o decimal

    def __repr__(self):
        return f"{self.nombre} (Poder: {self.poder})"

    def __add__(self, otra): #p1 + p2: combina poderes sumando (10 + 3)
        return Pocion(f"Mix de {self.nombre} + {otra.nombre}", self.poder + otra.poder)

    def __sub__(self, otra): #p1 - p2: resta el poder (10 - 3)
        return Pocion(f"{self.nombre} - {otra.nombre}", max(self.poder - otra.poder, 0))

    def __mul__(self, otra): #p1 * p2: multiplica poderes (10 × 3)
        return Pocion(f"{self.nombre} * {otra.nombre}", self.poder * otra.poder)

    def __floordiv__(self, otra): #p1 // p2: división entera (10 // 3 = 3)
        return Pocion(f"{self.nombre} // {otra.nombre}", self.poder // otra.poder)

    def __truediv__(self, otra): #p1 / p2: división decimal (10 / 3 ≈ 3.33)
        return Pocion(f"{self.nombre} / {otra.nombre}", round(self.poder / otra.poder, 2))

    def __mod__(self, otra): #p1 % p2: módulo, o lo que sobra (10 % 3 = 1)
        return Pocion(f"{self.nombre} % {otra.nombre}", self.poder % otra.poder)

    def __pow__(self, otra): #p1 ** p2: potencia (10³ = 1000)
        return Pocion(f"{self.nombre} ** {otra.nombre}", self.poder ** otra.poder)

# 🧪 Crear dos pociones mágicas
p1 = Pocion("Fuerza", 10)
p2 = Pocion("Agilidad", 3)

# 🧪 Aplicar operaciones
print("🧪 Suma:       ", p1 + p2)
print("🧪 Resta:      ", p1 - p2)
print("🧪 Multiplica: ", p1 * p2)
print("🧪 División //:", p1 // p2)
print("🧪 División / :", p1 / p2)
print("🧪 Módulo:     ", p1 % p2)
print("🧪 Potencia:   ", p1 ** p2)
