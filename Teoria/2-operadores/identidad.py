# IDENTIDAD: is -> TRUE si X e Y son el mismo objeto.
# IDENTIDAD: is not -> TRUE si X e Y NO son el mismo objeto.

"""
stdin  | 0 | Entrada estándar (por terminal)
stdout | 1 | Salida estándar (por terminal)
stderr | 2 | Error estándar (por terminal)
"""

texto1 = input("Introduce texto: ")

texto2 = input("Introduce texto: ")

print("IDENTIDAD: ", texto1 is texto2) # False -> Aunque sea el mismo texto "Hola", las dos variables se guardan en diferentes sitios de memoria.
print("COMPARACIÓN: ", texto1 == texto2) # True -> Compara el valor de texto 1 con el valor de texto2. hola == hola
