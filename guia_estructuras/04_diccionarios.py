# Seccion 5 - Diccionarios (dict)
alumno = {"nombre": "Ana", "edad": 20, "carrera": "Sistemas"}

print(alumno["nombre"])
alumno["edad"] = 21         # Actualizar
alumno["promedio"] = 9.2    # Agregar
del alumno["carrera"]       # Eliminar

# Recorrido
for clave, valor in alumno.items():
    print(clave, ":", valor)
