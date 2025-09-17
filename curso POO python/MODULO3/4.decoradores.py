#TOMA UNA FUNCION COMO ENTRADA, LE AGREGA UNA FUNCIONALIDAD EXTRA Y DEVUELVE UNA FUNCION MODIFICADA
#EL DECORADOR AGREGA FUNCIONALIDA ANTES O DESPUES

def decorador(funcion): #Funcion de entrada
    def funcionn_modificada(): #funcion extra
        print("Antes de llamar a la función")
        funcion() 
        print("Despues de llamar a la función")
    return funcionn_modificada

def saludo():
    print("Hola Rafael")

saludo_modificado = decorador(saludo)
saludo_modificado() #funcion modificada
