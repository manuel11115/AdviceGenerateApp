# Struct en Python (3) - dataclasses
from dataclasses import dataclass


@dataclass
class Mascota:
    nombre: str
    especie: str
    edad: int
    vacuna: str


m1 = Mascota("Firulais", "Perro", 3, "Rabia")
m2 = Mascota("Michi", "Gato", 2, "Triple Felina")

print(m1)
print(m2.nombre)
