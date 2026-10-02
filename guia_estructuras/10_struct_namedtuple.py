# Struct en Python (2) - namedtuple
from collections import namedtuple

Mascota = namedtuple("Mascota", ["nombre", "especie", "edad", "vacuna"])

m1 = Mascota("Firulais", "Perro", 3, "Rabia")
m2 = Mascota("Michi", "Gato", 2, "Triple Felina")

print(m1.nombre)   # Acceso por nombre
print(m2.vacuna)

try:
    m1.edad = 4
except AttributeError as e:
    print("Error esperado (namedtuple inmutable):", e)
