# Ejercicio 3 - Control de inventario
inventario = [
    {"producto": "Croquetas", "precio": 250, "stock": 20},
    {"producto": "Juguete", "precio": 100, "stock": 15},
    {"producto": "Shampoo", "precio": 180, "stock": 10},
]

# Calcular ingresos potenciales
total = 0
for item in inventario:
    subtotal = item["precio"] * item["stock"]
    print(f"{item['producto']}: {item['precio']} x {item['stock']} = {subtotal}")
    total += subtotal

print("Ingreso total si se vende todo:", total)
