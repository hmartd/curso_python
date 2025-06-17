
"""
- Ejercicio 04: Calculadora de gastos

Objetivo: Practicar funciones, conversión de strings a números (`int`, `float`), operaciones básicas y `return`

Instrucciones:
1. Crea una función llamada `calculate_total` que reciba tres argumentos:
   - `rent_str`, `food_str` y `transport_str`
2. Convierte los tres strings a números flotantes (`float`)
3. Calcula el total sumando los tres valores
4. La función debe devolver el total como `float`
5. Guarda el resultado de llamar a la función con `"750.50"`, `"245.75"` y `"60"` en una variable llamada `total`
6. Imprime la variable `total`

Requisitos:
- Usar funciones, argumentos, `return`
- Convertir correctamente strings a `float`
- Añadir un DocString a la función
"""

# Tu programa empieza aquí:

def calculate_total(rent_str, food_str, transport_str):
    """
    La función tiene tres argumentos. Convierte estos tres argumentos en float y luego retorna la suma de estos.

    Ejemplo:
    calculate_total("750.50", "245.75", "60") = 1056.25
    """
    total = float(rent_str) + float(food_str) + float(transport_str)
    return total

total = calculate_total("750.50", "245.75", "60")
print(total)