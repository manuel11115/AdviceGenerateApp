# Struct en Python (1) - Usando clases
class Mascota:
    def __init__(self, nombre, especie, edad, vacuna):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.vacuna = vacuna


m1 = Mascota("Firulais", "Perro", 3, "Rabia")
m2 = Mascota("Michi", "Gato", 2, "Triple Felina")

print(m1.nombre, "-", m1.vacuna)
print(m2.nombre, "-", m2.vacuna)
