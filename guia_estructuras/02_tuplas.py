# Seccion 3 - Tuplas (tuple)
coordenadas = (35.67, -120.45)
print("Coordenadas:", coordenadas)

# Ejemplo - Puntos geograficos
ciudad = ("León", 21.12, -101.68)
print(f"Ciudad: {ciudad[0]}, Latitud: {ciudad[1]}")

# Inmutabilidad: intentar modificar produce error
try:
    ciudad[1] = 0
except TypeError as e:
    print("Error esperado (tupla inmutable):", e)
