"""
Decorators
=> Modifica el comportamiento de una función realizando una combinación de todas las propiedades de la función 
"""

def func():
    i = 10
    return i

var = func   # var apunta a la función func
print(var)   # aparece un espacio de memoria   |    Si fuese var = func() estaría llamando a la función func() y asignando el valor de retorno a var
print(var())  # 10

print("-" * 30)

def func2():
    print("HOLA CLASE")

def func3(function):
    print(function)
    function()

func3(func2) 

print("-" * 30)
print("DECORATORS")

def mi_func():
    print("Hola Mundo!")

def mi_decorator(function):
    def wrapper():
        print("Ejecuto antes de la invocación de la función")
        function()
        print("Ejecuto después e la función invocada")
    return wrapper

mi_funcion_mod = mi_decorator(mi_func)
print(mi_funcion_mod) #<function mi_decorator.<locals>.wrapper at 0x0000018462BCC2C0> devuelve la dirección de memoria de la función
mi_funcion_mod()  # Ejecuta la función

print("-" * 30)
print("Decorators con condicionales")

def funcion():
    print("Hola Mundo")

def mi_decorator(func):
    def wrapper():
        if var4 < 5:
            func()
        else:
            print("Jajaja no lo vas a ejecutar")
    return wrapper

funcion = mi_decorator(funcion)

print("-"*10)
print("Synctactic Sugar")

def my_decorator(func):
    def wrapper():
        if n < 5:
            k = func() + n 
        else:
            print(f'ERROR: {n} es > 5')
            k = 0
        return k
    return wrapper

@my_decorator #  @my_decorator => function = my_decorator(function)
def my_function():
    print("init function")
    return 30

n = 2
print(my_function())