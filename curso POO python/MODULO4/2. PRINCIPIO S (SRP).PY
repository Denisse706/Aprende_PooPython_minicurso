#SRP
#SINGLE RESPONSABILITY PRINCIPLE
#CADA CLASE DE TENER UNA FUNCIONALIDAD UNICA

# Clase que solo guarda los datos del reporte
class Reporte:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido


# Clase que se encarga SOLO de imprimir
class Impresora:
    def imprimir(self, reporte):
        print("🖨️ Imprimiendo reporte:")
        print(f"Título: {reporte.titulo}")
        print(f"Contenido:\n{reporte.contenido}")
        print("-" * 30)


# Clase que se encarga SOLO de guardar el reporte en un archivo
class Guardador:
    def guardar(self, reporte):
        with open("reporte.txt", "w", encoding="utf-8") as archivo:
            archivo.write(f"{reporte.titulo}\n{reporte.contenido}")
        print("💾 Reporte guardado como 'reporte.txt'")
        print("-" * 30)


# Clase que se encarga SOLO de enviar el reporte por email
class Emailer:
    def enviar(self, reporte, email):
        print(f"📧 Enviando reporte '{reporte.titulo}' a {email}...")
        print("✅ Enviado (simulación)")
        print("-" * 30)


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    # Crear un objeto reporte
    mi_reporte = Reporte("Informe Mensual", "Ventas: $10,000\nCostos: $4,000")

    # Imprimir
    impresora = Impresora()
    impresora.imprimir(mi_reporte)

    # Guardar
    guardador = Guardador()
    guardador.guardar(mi_reporte)

    # Enviar
    emailer = Emailer()
    emailer.enviar(mi_reporte, "cliente@empresa.com")
