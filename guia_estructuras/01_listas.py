# Seccion 2 - Listas (list)
frutas = ["manzana", "pera", "uva"]

print(frutas[0])            # Acceso: "manzana"
frutas.append("kiwi")       # Agregar
frutas.remove("pera")       # Eliminar
frutas[1] = "plátano"       # Actualizar
print(frutas)

# Recorrido
for fruta in frutas:
    print(fruta)

# Ejemplo practico - Registro de compras
compras = []
for i in range(3):
    producto = input("Producto: ")
    compras.append(producto)

print("Lista final:", compras)
