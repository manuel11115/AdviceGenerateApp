# Ejercicio 1 - Analisis de encuestas
lenguajes = ["Python", "C++", "Python", "Java", "Python", "C#"]

# Cuantos estudiantes dominan cada lenguaje (sin duplicados)
unicos = set(lenguajes)
for l in sorted(unicos):
    print(l, "→", lenguajes.count(l))

print("Lenguajes sin duplicados:", sorted(unicos))
