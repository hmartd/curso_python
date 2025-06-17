"""

break => sirve para romper un condicional

"""
colores = ["rojo", "azul", "verde"]

for color in colores:
    print(color)
    break

n = 5

while n > 0:
    print(n)
    n -= 1
    break

for color in colores:
    print(color)
    break
else:
    print("Printa Else")

# En el caso de arriba solo imprimiría rojo puesto que else forma parte del for y break sale del for.

print("-" * 5)
for color in colores:
    if (color == "azul"):
        break  # Sale del del for cuando el color es azul. Imprime solo rojo
    print(color)

"""
pass
Define el esquelo de las estructuras
"""

print("-" * 10)
print("pass")

def func():
    pass

colores = ["rojo", "azul", "verde"]

for color in colores:
    # No se que se va a realizar
    pass