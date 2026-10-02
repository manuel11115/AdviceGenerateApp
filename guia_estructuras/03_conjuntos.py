# Seccion 4 - Conjuntos (set)
materias = {"Matemáticas", "Física", "Programación"}

# Operaciones
materias.add("Inglés")
materias.discard("Física")
print("Programación" in materias)
print(sorted(materias))

# Operaciones matematicas
a = {"Python", "C++", "Java"}
b = {"Python", "JavaScript"}
print(sorted(a.union(b)))         # Union
print(sorted(a.intersection(b)))  # Interseccion
