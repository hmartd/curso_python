# LÓGICOS: Modifican expresiones evaluadas en un contexto de TRUE/FALSE para crear condiciones más complejas
# 'not' -> (not X) TRUE si X es False | FALSE si X es True
# 'or' -> (x or y) TRUE si X or Y son verdaderas (una de las dos)
# 'and' -> (x and y) TRUE solo si X e Y son verdaderas

# NOT 

num = 5
print(num < 10) # TRUE
print("NOT ", not num < 10) # NOT TRUE -> FALSE

# OR

num1 = 5
num2 = 10
print(num1 < 4) # FALSE
print("OR ", num1 < 4 or num2 > 5) # FALSE OR TRUE = TRUE

# AND

num1 = 5
num2 = 10
print(num1 < 4) # FALSE
print("AND ", num1 < 4 and num2>5) # FALSE AND TRUE = FALSE