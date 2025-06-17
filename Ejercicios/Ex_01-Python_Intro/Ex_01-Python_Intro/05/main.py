
"""
- Ejercicio 05: Conversor y promedio de temperaturas

Objetivo: Practicar funciones, conversión de strings a números (`float`), cálculos y `return`.

Instrucciones:
1. Crea una función llamada `convert_and_average` que reciba tres strings:
   - `t1`, `t2` y `t3`, que representan temperaturas en grados Celsius.
2. Convierte los tres valores a `float`.
3. Calcula el promedio (media) de las tres temperaturas.
4. La función debe devolver un string con el siguiente formato:
   "La temperatura media es <valor> grados Celsius"
   (donde <valor> debe tener 2 decimales).
5. Guarda el resultado de llamar a la función con `"22.5"`, `"19.0"` y `"25.3"` en una variable llamada `result`.
6. Imprime la variable `result`.

Requisitos:
- Usar funciones, argumentos, `return`.
- Usar `float()` y `round()` con 2 decimales.
- Añadir un docstring a la función.
"""

# Tu programa empieza aquí:

def convert_and_average(t1,t2,t3):
    """
    La función calcula la media de los tres argumentos. Y retorna un mensaje.

    Ejemplo: 
    convert_and_average("22.5", "19.0", "25.3") = "La temperatura media es 22.27 grados Celsius"
    """
    t1= float(t1)
    t2= float(t2)
    t3= float(t3)

    average = round((t1 + t2 + t3) / 3, 2) # round(numero, con cuantos decimales) quieres redondear
    return f"La temperatura media es {average} grados Celsius"

result = convert_and_average("22.5", "19.0", "25.3")
print(result)