"""Herencia"""

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
        self._combustible = "l/100km"

    def especificaciones(self):
        """Muestra las especificaciones del coche"""             
        print(f"Marca: {self._marca}\
              \nModelo: {self._modelo}\
              \nPotencia: {self._potencia} cv\
              \nVelocidad Máxima: {self._vel_max} km/h\
              \nConsumo Medio: {self._con_medio} {self._combustible}\
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

print("\nCoche Tesla (Clase Coche -> padre)\n" +"-"*30)
tesla = Coche("Tesla", "Model X", 300, 360, 15) # 15Kwh/100km
tesla.especificaciones() # Las especificaciones están mal puesto que Tesla no tiene 15 l/100km, tiene 15Kwh/100km al ser eléctrico


class CocheElectrico(Coche): # Coche es la clase padre y CocheElectrico es la clase hijo.
    """Esta clase representa un coche eléctrico"""
    
    def __init__(self, marca, modelo, potencia, vel_max, con_medio, capacidad_bateria):
        """Inicializa los atributos de la clase padre"""
        super().__init__(marca, modelo, potencia, vel_max, con_medio)
        self._combustible = "KWh/100km"
        self._capacidad_bateria = capacidad_bateria

    def detalles_bateria(self):
        """Muestra detalles de la bateria del coche"""
        print(f"El tamaño de la bateria es {self._capacidad_bateria} KWh")

    def consumo_total(self):
        """Muestra el consumo total desde el Kilometro 0"""
        consumo_total = (self._km_actuales / 100) * self._con_medio
        print(f"El consumo total es de {consumo_total} KWh")


print("\nCoche Tesla (Clase CocheEléctrico -> hijo)\n" +"-"*30)
tesla = CocheElectrico("Tesla", "Model X", 300, 360, 15, 500)

tesla.kilometros = 200
tesla.especificaciones()
tesla.detalles_bateria()
tesla.consumo_total()
