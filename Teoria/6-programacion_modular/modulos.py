"""
Modulos
- Este escrito en Python
- Está escrito en C y cargado dinámicamente
- Incorporado en el interpreter

Acceder al contenido de un Modulo: 'import'
Modulo Python = fichero.py

"""

import mi_modulo

var = mi_modulo.string # Importar una variable
print(var)

bmw = mi_modulo.Coche() # Importar una clase del fichero mi_modulo.py
mi_modulo.my_function(var) # Importar una función