"""
Variables globales: MAYUSCULAS
Variables locales: minusculas
Atributos: _atributo
"""

class Coche:
    """Esta es una clase que representa un coche"""

    def __init__(self, marca, modelo, potencia, vel_max, con_medio):
        """Iniciliza los atributos
        Argumentos posicionales:
        marca - str marca del coche
        modelo - str modelo del coche
        potencia - int potencia del coche en CV
        vel_max - int velocidad maxima del coche km/h
        con_medio - float consumo medio del coche en l/100km
        """
        self._marca = marca             # cuando una variable es un atributo se pone _ antes de la variable
        self._modelo = modelo
        self._potencia = potencia
        self._vel_max = vel_max
        self._con_medio = con_medio
        self._km_actuales = 0

    def especificaciones(self):
        """Muestra las especificaciones del coche"""
        # print("Potencia {}".format(self.potencia)) # Formatea todo a string
        # print(f"Potencia {self.potencia}")
        """print("Marca: ",self.marca,
              "\nModelo: ",self.modelo,
              "\nPotencia: {} cv".format(self.potencia),
              "\nVelocidad Máxima: {} km/h".format(self.vel_max),
              "\nConsumo Medio: {} l/100km".format(self.con_medio))"""
        
        print(f"Marca: {self._marca}\
              \nModelo: {self._modelo}\
              \nPotencia: {self._potencia} cv\
              \nVelocidad Máxima: {self._vel_max} km/h\
              \nConsumo Medio: {self._con_medio} l/100km\
              \nKilometros Actuales: {self._km_actuales} km")
        
    def actualizar_kilometros(self, kilometros_nuevos): # SETTER
        """Actualizar los kilometros"""
        if kilometros_nuevos > self._km_actuales:
            self._km_actuales = kilometros_nuevos
        else:
            print("ERROR: No se puede ir atrás en kilometraje")
    
    def consumo_total(self): # GETTER
        """Muestra el consumo real del coche desde el kilometro 0"""
        consumo_total = (self._km_actuales / 100) * self._con_medio
        print(f"El consumo total del coche es de {consumo_total} litros")

mercedes = Coche("Mercedes", "C200", 200, 240, 7.5)
mercedes.especificaciones()
# help(Coche)
print("-"*30)

mercedes.km_actuales = 45_000
mercedes.especificaciones()
print("-"*30)

mercedes.actualizar_kilometros(30_000)
mercedes.especificaciones()
print("-"*30)

mercedes.actualizar_kilometros(30_000)
mercedes.especificaciones()
mercedes.consumo_total()
print("-"*30)