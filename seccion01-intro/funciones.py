# Funciones

# Funciones en matematicas y = f(x)

var = "Hola Mundo"

var_len = len(var) # Longitud de la variable var 
print(var_len)

def mi_funcion(arg1,arg2):
    print(arg1)
    print(arg2)

mi_funcion("ey","tú")

def print_algo():
    print("Algo")

print_algo()

# Argumentos de una Función
# 1. Posicional | Requeridos para funcionar

def funcion_3_argumentos(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

funcion_3_argumentos("Platano", "Fresa", "Manzana")


# 2. Palabras Clave

def mi_funcion_key(arg1, arg2):
    print(arg1)
    print(arg2)

var = "Key1" 
var2 = "Key2"

mi_funcion_key(var, var2)

# Valores por defecto

def mi_funcion_def(arg1, arg2="Defecto"):
    print(arg1, arg2)

mi_funcion_def("Sandía") # Sandía  Defecto
mi_funcion_def("Melon", 10) # Melon 10 (si no se define el arg2 por defecto está el valor "Defecto", si se define un arg2 toma ese valor)

# Return

def mi_funcion_return():
    return 10

var = mi_funcion_return()
print(var)

def abc():
    return 1,2,3

a, b, c = abc()
print(a,b,c)

def login (a, b):
    """
    Esta función es un login que va ha recibir dos argumentos 

    a = Mail
    b = Password
    """
    print(a)
    print(b)

# Se va a inicializar la función login
a = "correo@mail.com"
b = "password"

login(a, b)