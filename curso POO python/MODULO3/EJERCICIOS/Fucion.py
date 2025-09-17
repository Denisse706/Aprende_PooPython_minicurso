class Personaje:
    def __init__(self, nommbre, fuerza, velocidad):
        self.nombre = nommbre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __str__(self):
        return f"Personaje: {self.nombre}, su fuerza es: {self.fuerza} y su velocidad es {self.velocidad}"
    
    def __add__(self, otro):
        new_nombre = self.nombre + "-" + otro.nombre
        new_fuerza = round(((self.fuerza + otro.fuerza)/2)**1.5)
        new_velocidad = round(((self.velocidad + otro.velocidad)/2)**1.5)
        return Personaje(new_nombre, new_fuerza, new_velocidad)

goku = Personaje("Goku", 100, 100)
vegeta = Personaje("Vegeta", 200, 100)
goketa = goku + vegeta
print(goketa.velocidad)
