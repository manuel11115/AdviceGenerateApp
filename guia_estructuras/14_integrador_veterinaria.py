# Ejercicio integrador final - Gestion de una veterinaria
# Usa listas y diccionarios combinados.
PRECIOS = {"Rabia": 250.0, "Triple Felina": 300.0, "Parvovirus": 220.0, "Moquillo": 180.0}

mascotas = []  # lista de diccionarios


def registrar():
    nombre = input("Nombre: ").strip()
    tipo = input("Tipo (perro/gato/...): ").strip()
    edad = int(input("Edad: "))
    print("Vacunas disponibles:", ", ".join(f"{v} (${p})" for v, p in PRECIOS.items()))
    vacuna = input("Vacuna aplicada: ").strip()
    if vacuna not in PRECIOS:
        print("Vacuna no válida, no se registró.")
        return
    mascotas.append({"nombre": nombre, "tipo": tipo, "edad": edad, "vacuna": vacuna})
    print(f"Mascota {nombre} registrada.")


def buscar():
    nombre = input("Nombre a buscar: ").strip().lower()
    encontradas = [m for m in mascotas if m["nombre"].lower() == nombre]
    if not encontradas:
        print("No encontrada")
    for m in encontradas:
        print(f"{m['nombre']} - {m['tipo']} - {m['edad']} años - vacuna: {m['vacuna']}")


def estadisticas():
    conteo = {}
    for m in mascotas:
        conteo[m["vacuna"]] = conteo.get(m["vacuna"], 0) + 1
    print("Vacunas aplicadas:")
    for vacuna, n in conteo.items():
        print(f"  {vacuna}: {n}")
    print("Total de vacunas:", sum(conteo.values()))


def ingreso_total():
    desglose = {}
    for m in mascotas:
        desglose[m["vacuna"]] = desglose.get(m["vacuna"], 0) + PRECIOS[m["vacuna"]]
    for vacuna, monto in desglose.items():
        print(f"  {vacuna}: ${monto}")
    print("Ingreso total:", sum(desglose.values()))


acciones = {"1": registrar, "2": buscar, "3": estadisticas, "4": ingreso_total}

while True:
    print("\n--- VETERINARIA ---\n1) Registrar  2) Buscar  3) Estadísticas  4) Ingreso total  5) Salir")
    op = input("Opción: ")
    if op == "5":
        break
    acciones.get(op, lambda: print("Opción inválida"))()
