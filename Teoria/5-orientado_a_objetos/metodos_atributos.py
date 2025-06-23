"""
Método
=> Funciones dentro de una clase
"""

class Coche:
    def velocidad_maxima(self): # self -> se llama a si misma. Para los métodos de las clases (funciones dentro de la clase) siempre ha de haber un argumento. Si no devuelve nada hay que poner self.
        """Retorna la v_max del coche"""
        print("Velocidad Maxima: ")


coche1 = Coche()

print(coche1)

coche1.velocidad_maxima()