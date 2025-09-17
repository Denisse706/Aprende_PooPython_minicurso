class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __add__(self, otra_cuenta):
        nuevo_titular = f"{self.titular} & {otra_cuenta.titular}"
        nuevo_saldo = self.saldo + otra_cuenta.saldo
        return CuentaBancaria(nuevo_titular, nuevo_saldo)

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: ${self.saldo:.2f}"


# Crear dos cuentas
cuenta1 = CuentaBancaria("Alice", 1500)
cuenta2 = CuentaBancaria("Bob", 2000)
cuenta3 = CuentaBancaria("Mercury", 3000)

# Sumar las cuentas
cuenta_combinada = cuenta1 + cuenta2 + cuenta3

# Mostrar resultados
print("Cuenta 1:", cuenta1)
print("Cuenta 2:", cuenta2)
print("Cuenta 2:", cuenta3)
print("Cuenta combinada:", cuenta_combinada.titular)
