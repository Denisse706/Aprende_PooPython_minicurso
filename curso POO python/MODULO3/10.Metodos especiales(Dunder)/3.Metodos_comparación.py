class Jugador:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def __repr__(self):
        return f"{self.nombre} (Nivel {self.nivel})"

    def __lt__(self, otro): #"Less than" → <
        return self.nivel < otro.nivel

    def __gt__(self, otro): #__gt__: "Greater than" → >
        return self.nivel > otro.nivel

    def __le__(self, otro): #__le__: "Less or equal" → <=
        return self.nivel <= otro.nivel

    def __ge__(self, otro): #__ge__: "Greater or equal" → >=
        return self.nivel >= otro.nivel

    def __eq__(self, otro): #__eq__: "Equal" → ==
        return self.nivel == otro.nivel

    def __ne__(self, otro): #__ne__: "Not equal" → !=
        return self.nivel != otro.nivel
#Cada uno devuelve True o False según el valor de .nivel.

# 🧪 Probamos
j1 = Jugador("Alice", 5)
j2 = Jugador("Bob", 8)
j3 = Jugador("Charlie", 5)

print(j1, "<", j2, "=", j1 < j2)      # True
print(j2, ">", j3, "=", j2 > j3)      # True
print(j1, "<=", j3, "=", j1 <= j3)    # True
print(j2, ">=", j1, "=", j2 >= j1)    # True
print(j1, "!=", j3, "=", j1 != j3)    # False
print(j1, "==", j3, "=", j1 == j3)    # True
