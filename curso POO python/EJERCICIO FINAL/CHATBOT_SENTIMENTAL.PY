from transformers import pipeline
from colorama import init, Fore, Style

# Inicializamos colorama
init(autoreset=True)

# Cargamos el modelo de emociones
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

# Mapeo de emociones a colores y etiquetas en español
emociones_colores = {
    "sadness": ("triste", Fore.BLUE),
    "anger": ("enojado", Fore.RED),
    "joy": ("feliz", Fore.YELLOW),
    "neutral": ("neutral", Fore.GREEN),
}

def detectar_emocion(texto):
    resultado = emotion_classifier(texto)  # resultado es [[{...}]]
    emocion_dict = resultado[0][0]         # Accedemos correctamente al primer dict
    emocion_original = emocion_dict['label']
    
    emocion_es, color = emociones_colores.get(emocion_original, ("desconocido", Fore.WHITE))

    print(color + f"Parece que estás {emocion_es}.")
    
# Bucle principal
print("Escribe lo que sientes. Escribe 'salir' para terminar.")
while True:
    texto_usuario = input("Tú (solo entiendo respuestas en ingles): ")
    if texto_usuario.lower() == "salir":
        print("¡Hasta pronto!")
        break
    detectar_emocion(texto_usuario)





