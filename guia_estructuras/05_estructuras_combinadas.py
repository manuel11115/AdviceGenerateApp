# Seccion 6 - Estructuras combinadas: registro de estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 20, "promedio": 9.1},
    {"nombre": "Luis", "edad": 22, "promedio": 8.5},
    {"nombre": "María", "edad": 21, "promedio": 9.3},
]

for est in estudiantes:
    print(f"{est['nombre']} tiene promedio {est['promedio']}")
