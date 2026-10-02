# Ejemplo practico combinado - Veterinaria con dataclass
from dataclasses import dataclass


@dataclass
class Mascota:
    nombre: str
    especie: str
    edad: int
    vacuna: str
    costo: float


registro = [
    Mascota("Firulais", "Perro", 3, "Rabia", 250.0),
    Mascota("Michi", "Gato", 2, "Triple Felina", 300.0),
    Mascota("Max", "Perro", 1, "Parvovirus", 220.0),
]

total = 0
for m in registro:
    print(f"{m.nombre} ({m.especie}) - Vacuna: {m.vacuna} - ${m.costo}")
    total += m.costo
print("\nTotal ingresos:", total)
