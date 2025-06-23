"""Decorators en Clases"""

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
        print(f"Marca: {self._marca}\
              \nModelo: {self._modelo}\
              \nPotencia: {self._potencia} cv\
              \nVelocidad Máxima: {self._vel_max} km/h\
              \nConsumo Medio: {self._con_medio} l/100km\
              \nKilometros Actuales: {self._km_actuales} km")

    @property    
    def kilometros(self):
        return self._km_actuales

    @kilometros.setter    
    def kilometros(self, kilometros): # SETTER : Añade información
        """Actualizar los kilometros"""
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else:
            print("ERROR: No se puede ir atrás en kilometraje")
    
    @kilometros.getter
    def consumo_total(self): # GETTER : Da información
        """Muestra el consumo real del coche desde el kilometro 0"""
        consumo_total = (self._km_actuales / 100) * self._con_medio
        print(f"El consumo total del coche es de {consumo_total} litros")


bmw = Coche("BMW", "X5", 220, 250, 15.2)
print("\nEspecificaciones Iniciales\n"+"-"*30)
bmw.especificaciones()

bmw.kilometros = 15_000
print("\nEspecificaciones Actualizadas\n"+"-"*30)
bmw.especificaciones()



