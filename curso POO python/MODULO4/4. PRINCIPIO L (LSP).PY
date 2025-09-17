#LSP
#LISKOV'S SUSTITUTION PRINCIPLE
#Una clase hija debe poder sustituir a su clase padre sin alterar el funcionamiento del programa.
#En otras palabras, si una función espera una clase base, también debería funcionar perfectamente si se le pasa una subclase.

# Clase base correcta
class Pajaro:
    def hacer_sonido(self):
        print("🐤 Pío pío")

# Subclases que respetan el contrato
class Gorrion(Pajaro):
    def volar(self):
        print("🐦 Gorrion volando bajo...")

class Pinguino(Pajaro):
    def nadar(self):
        print("🐧 Pinguino nadando rápido...")

# Función que acepta un Pajaro, sin depender de habilidades que no todos tienen
def saludar_pajaro(pajaro: Pajaro):
    pajaro.hacer_sonido()

# FUNCIONES ESPECÍFICAS
def volar_si_puede(pajaro):
    if hasattr(pajaro, "volar"):
        pajaro.volar()

def nadar_si_puede(pajaro):
    if hasattr(pajaro, "nadar"):
        pajaro.nadar()


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    print("--- DEMOSTRACIÓN DEL PRINCIPIO LSP ---")

    gorrion = Gorrion()
    pinguino = Pinguino()

    saludar_pajaro(gorrion)
    saludar_pajaro(pinguino)

    volar_si_puede(gorrion)
    nadar_si_puede(pinguino)
#✅ ¿Por qué el segundo ejemplo sí cumple LSP?
#Nunca forzamos a una subclase a hacer lo que no puede (como volar si no vuela).
#Cada subclase respeta y extiende la funcionalidad sin romper el sistema.
#Las funciones genéricas (saludar_pajaro) funcionan igual para todas las subclases.

