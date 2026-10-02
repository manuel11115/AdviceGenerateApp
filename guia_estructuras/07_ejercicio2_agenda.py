# Ejercicio 2 - Agenda digital (agregar, buscar, eliminar, listar)
agenda = {"Ana": "4771234567", "Luis": "4778901234"}


def agregar():
    nombre = input("Nombre a agregar: ")
    agenda[nombre] = input("Teléfono: ")
    print(f"Contacto {nombre} agregado.")


def buscar():
    nombre = input("Nombre a buscar: ")
    if nombre in agenda:
        print(f"Teléfono: {agenda[nombre]}")
    else:
        print("No encontrado")


def eliminar():
    nombre = input("Nombre a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("No encontrado")


def listar():
    for nombre, tel in agenda.items():
        print(f"{nombre}: {tel}")


acciones = {"1": agregar, "2": buscar, "3": eliminar, "4": listar}

while True:
    print("\n--- AGENDA ---\n1) Agregar  2) Buscar  3) Eliminar  4) Listar  5) Salir")
    op = input("Opción: ")
    if op == "5":
        break
    acciones.get(op, lambda: print("Opción inválida"))()
