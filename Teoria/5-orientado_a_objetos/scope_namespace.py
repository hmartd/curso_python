"""
NameSpace
=> Mapeo de los nombres de los objetos. Se crean en diferentes momentos
    y tienen diferente tiempos de vida
=> A los NameSpace se accede mediante scopes
=> Python crea el NameSpace por defecto y nunca se borra
"""

# print(dir(__builtins__))

# NameSpace globals dura hasta que se cierra el interpreter
var_modulo = 10

# print(globals()) => Imprime las variables de entorno globales de mi programa NameSpace

# Namespace locals dura hasta que acaba la función

def fun():
    var_local = 5
    print(locals()) # Imprime las variables locales de mi programa NameSpace


fun() 


"""
Scope 
=> Región de un programa dese donde se accede a un NameSpace directamente
"""

# Scope Locales 

def func():
    var_local_fun = 10
    print(var_local_fun)

func()

# Scope NO Local

def func():
    var_no_local = 10
    print("NameSpace", locals())
    def func2():
        var_local = 5
        var_local_1 = var_no_local + 1 # Si llamo a la variable no local, se añade a las variables locales. Luego crea una variable local var_local_1 que tiene como valor: (var_no_local + 1)
        print("NameSpace", locals()) 
    func2()

func() # NameSpace {'var_no_local': 10}
       # NameSpace {'var_local': 5, 'var_local_1': 11, 'var_no_local': 10}

print("-"*10)
var_global = 89
def func3():
    def func4():
        var_global = 90
        print(var_global)
        print(locals())
        print(globals())
    func4()

func3()
print(var_global)

print("-"*10)
# Gloabl / Non Local
contador = 0 # VARIABLE GLOBAL

def actualizar_contador():
    global contador # Damos permiso de escritura a la variable contador que está en global. Es decir, está fuera de la función.
    while contador < 10:
        print(contador)
        contador += 1

actualizar_contador()
print("Valor contador:",contador) # La variable contador se ha actualizado en la función actualizar_contador() porque ha tenido permisos de escritura.

def fun_contador():
    cont = 0 # VARIABLE NONLOCAL
    def act_contador():
        nonlocal cont # Damos permiso de escritura a la variable cont que está en nonlocal. Es decir, está en la función de afuera.
        while cont < 10:
            print(cont)
            cont += 1
    act_contador()
    print("Valor cont:", cont)

fun_contador()