from math import e


# Ejercicio 1 - ReLu

def relu (x):
    """
    Calcula el resultado de aplicar la función ReLu sobre una entrada x.
    """
    return max(0, x)


entrada = input("Introduce un valor numérico: ")
resultado = relu(float(entrada))
print(f"El resultado de aplicar la función ReLu(x) sobre {entrada} es:", resultado)


# Ejercicio 2 - Sigmoid

def sigmoid(x):
    """
    Calcula el resultado de aplicar la función Sigmoid sobre una entrada x.
    """
    return 1/(1+e**(-x))


resultado = sigmoid(float(entrada))
print(f"El resultado de aplicar la función Sigmoid(x) sobre {entrada} es:", resultado)


# Ejercicio 3 - Tanh

def tanh(x):
    """
    Calcula el resultado de aplicar la función Tanh sobre una entrada x.
    """
    sinh = (e**x-e**(-x))/2
    cosh = (e**x+e**(-x))/2
    return sinh/cosh

resultado = tanh(float(entrada))
print(f"El resultado de aplicar la función Tanh(x) sobre {entrada} es:", resultado)