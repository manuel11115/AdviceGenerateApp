# Struct en Python (4) - modulo struct (manejo binario)
import struct

# Empaquetar datos (entero y flotante) en formato binario
data = struct.pack('if', 25, 3.14)   # i = int, f = float
print("Datos empaquetados:", data)

# Desempaquetar los datos
valor = struct.unpack('if', data)
print("Datos originales:", valor)
