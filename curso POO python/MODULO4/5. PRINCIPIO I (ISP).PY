#ISP
#INTERFACE SEGREGATION PRINCIPLE
#Las interfaces (o clases base) deben ser pequeñas y específicas.
#Es mejor tener muchas interfaces pequeñas que una grande que obligue a implementar métodos innecesarios.

class Trabaja:
    def trabajar(self):
        pass

class Come:
    def comer(self):
        pass

class Duerme:
    def dormir(self):
        pass

# Clases que implementan solo lo que necesitan
class Humano(Trabaja, Come, Duerme):
    def trabajar(self):
        print("🧑‍💼 Humano trabajando...")

    def comer(self):
        print("🥗 Humano comiendo...")

    def dormir(self):
        print("😴 Humano durmiendo...")

class Robot(Trabaja):
    def trabajar(self):
        print("🤖 Robot trabajando sin descanso...")

# --- PROGRAMA VISUAL ---
def rutina(trabajador):
    trabajador.trabajar()
    if isinstance(trabajador, Come):
        trabajador.comer()
    if isinstance(trabajador, Duerme):
        trabajador.dormir()

# Demostración
print("=== Rutina del HUMANO ===")
rutina(Humano())

print("\n=== Rutina del ROBOT ===")
rutina(Robot())

#✅ ¿Por qué sí cumple ISP?
#Cada clase implementa solo lo que necesita.
#Robot no está obligado a implementar cosas humanas.
#Es más fácil mantener y escalar el código.