#DIP
#DEPENDENCY INVERSION PRINCIPLE
#Las clases de alto nivel no deben depender de clases de bajo nivel. Ambas deben depender de abstracciones.
#El código debe depender de interfaces o abstracciones, no de implementaciones concretas.
# Esto hace que el sistema sea más flexible, desacoplado y fácil de cambiar o extender.

# Abstracción
class Motor:
    def encender(self):
        pass

# Implementaciones concretas
class MotorGasolina(Motor):
    def encender(self):
        print("⛽ Motor de gasolina encendido.")

class MotorElectrico(Motor):
    def encender(self):
        print("🔋 Motor eléctrico encendido.")

# Clase de alto nivel que depende de la abstracción, no de una implementación
class Auto:
    def __init__(self, motor: Motor):
        self.motor = motor  # ✅ Inyección de dependencia

    def arrancar(self):
        self.motor.encender()

# --- USO VISUAL ---
print("🚙 Auto con motor de gasolina:")
auto1 = Auto(MotorGasolina())
auto1.arrancar()

print("\n🚗 Auto con motor eléctrico:")
auto2 = Auto(MotorElectrico())
auto2.arrancar()
#✅ ¿Por qué este ejemplo cumple DIP?
#Auto depende de la interfaz Motor, no de una clase concreta.
# Puedes agregar nuevos tipos de motores sin tocar la clase Auto.
# Mayor flexibilidad, mantenimiento y extensión del código.

