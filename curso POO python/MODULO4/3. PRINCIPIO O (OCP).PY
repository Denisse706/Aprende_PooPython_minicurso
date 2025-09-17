#OCP
#OPEN/ CLOSED PRINCIPLE (EL CODIGO DEBE ESTAR ABIERTO PARA EXTENSION PERO CERRADO PARA MODIFICACION)
#LAS ENTIDADES DE SORTWARE (CLASES, MMODULOS, FUNCIONES, ETC) DEBEN ESTAR ABIERTAS PARA LA EXTENSION PERO CERRADAS PARA LA MODIFICACION
#DEBERIAMOS PODER AGREGARLE NUEVAS FUNCIONALIDADES, SIN TENER QUE CAMBIAR EL CODIGO FUENTE DE LAS ENTIDADES
#SE TRATA CREAR PARTES MAS PEQUEÑAS DEL PROGRAMA PARA QUE AL AGREGAR NUEVAS FUNCIONALIDADES
#SOLO SE TENGA QUE AÑADIR LOS CAMBIOS SIN MODIFICAR TODO EL CODIGO ORIGINAL

# Clase base - cerrada para modificación
class ProcesadorPago:
    def pagar(self, monto):
        raise NotImplementedError("Debes implementar el método 'pagar'")

# Subclases - abiertas para extensión
class PagoEfectivo(ProcesadorPago):
    def pagar(self, monto):
        print(f"💵 Pagando ${monto} en EFECTIVO")

class PagoTarjeta(ProcesadorPago):
    def pagar(self, monto):
        print(f"💳 Pagando ${monto} con TARJETA de crédito")

class PagoPayPal(ProcesadorPago):
    def pagar(self, monto):
        print(f"🌐 Pagando ${monto} con PAYPAL")

# Puedes añadir más formas sin modificar las anteriores
class PagoBitcoin(ProcesadorPago):
    def pagar(self, monto):
        print(f"₿ Pagando ${monto} con BITCOIN")

# Función que realiza un pago, sin importar el método
def procesar_pago(pago: ProcesadorPago, monto: float):
    pago.pagar(monto)


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    print("--- SIMULACIÓN DE PAGOS (OCP) ---")

    monto = 100

    efectivo = PagoEfectivo()
    tarjeta = PagoTarjeta()
    paypal = PagoPayPal()
    bitcoin = PagoBitcoin()

    procesar_pago(efectivo, monto)
    procesar_pago(tarjeta, monto)
    procesar_pago(paypal, monto)
    procesar_pago(bitcoin, monto)

#✅ ¿Por qué cumple con OCP?
#No se modifica ProcesadorPago ni las clases existentes.
#Se extiende el sistema agregando nuevas formas de pago (PagoBitcoin, PagoQR, etc.).
#La función procesar_pago() no cambia: solo recibe cualquier clase hija.

