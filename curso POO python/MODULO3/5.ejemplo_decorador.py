def contador_llamadas(func):
    #🔹 *args: Recibe una lista de argumentos no nombrados (posicionales).
    #🔹 **kwargs: Recibe un diccionario de argumentos nombrados (clave=valor).
    #📌 ¿Cuándo se usan? Cuando no sabes cuántos argumentos va a recibir una función, o quieres que sea flexible.

    def wrapper(*args, **kwargs):#🧩 1. ¿Qué es un wrapper? Un wrapper (envoltorio) es una función 
        #interna dentro de un decorador que envuelve la función original para modificar o extender 
        # su comportamiento sin modificar su código original.

#📦 ¿Cuándo lo usas? Cuando quieres añadir funcionalidad
# extra a una función (como contar llamadas, verificar permisos, medir tiempo, etc.).
        wrapper.contador += 1
        print(f"La función '{func.__name__}' ha sido llamada {wrapper.contador} veces.")
        return func(*args, **kwargs)
    
    wrapper.contador = 0  # Inicializamos el contador
    return wrapper

@contador_llamadas  #🧩 3. ¿Qué es @contador o @algo?
#El símbolo @ se llama "syntactic sugar" (azúcar sintáctico). Es una forma más limpia de escribir:
def saludar():
    print("¡Hola!")

@contador_llamadas
def despedirse():
    print("¡Adiós!")

# Pruebas
saludar()
saludar()
despedirse()
saludar()