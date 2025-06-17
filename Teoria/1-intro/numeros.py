# Números Enteros int() -> No tienen decimales

num = 10
num2 = "12"

num3 = int(num2) # Un String puede convertirse a un entero

num4 = num3 + 4
print(num4)

# Números grandes

numg = 1000000
print(numg)

numg2 = 1_000_000
print(numg2) # Imprime el valor 1000000. numg == numg2

if numg == numg2:
    print('true')
else:
    print('false')

# Número flotantes | Decimales float()

numf = 10.5 
numf = numf + 3
print(numf)

numf2 = "9.4"
numf2 = float(numf2)
numf2 = numf2 + 3
print(numf2)

numfg = 1000000.3 # 1ra forma de representar un número grande
numfg2 = 1_000_500.4 # 2a forma de representar un número grande
numfg3 = 1e6 # 3a forma de representar número (1 elevado a 6) -> 1000000.0
print(numfg3)

# Max y Min de Float (Los números decimales tienen un máximo y un mínimo porque ocupan mucho más espacio en la memoria 

num_Max_f = 2e400 
print(num_Max_f) # Da inf de infinito. Es el máximo

num_Min_f = -2e400
print(num_Min_f) # Da -inf de -infinito. Es el mínimo

# Números Complejos

num_Comp = 1 + 2j
print(num_Comp) # Imprime 1+2j

print(num_Comp.real) # Imprime 1.0 que es la parte real
print(num_Comp.imag) # Imprime que 2.0 es la parte imaginaria

num_Comp2 = num_Comp.real + 1
print(num_Comp2)

num_Comp = num_Comp + 5 # Suma 5 a la parte real, 1+5= 6 -> 6+2j
print(num_Comp)
