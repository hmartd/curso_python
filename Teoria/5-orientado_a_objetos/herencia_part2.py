# CLASE PADRE

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


# CLASE HIJO

class CocheElectrico(Coche): 
    """Esta clase representa un coche eléctrico"""
    
    def __init__(self, marca, modelo, potencia, vel_max, con_medio, bateria):
        """Inicializa los atributos de la clase padre"""
        super().__init__(marca, modelo, potencia, vel_max, con_medio)
        self._combustible = "KWh/100km"
        self._bateria = bateria

    def detalles_bateria(self):
        """Muestra detalles de la bateria del coche"""
        self._bateria.especificaciones_bateria()

    def consumo_total(self):
        """Muestra el consumo total desde el Kilometro 0"""
        consumo_total = (self._km_actuales / 100) * self._con_medio
        print(f"El consumo total es de {consumo_total} KWh")



# CLASES ADICIONALES - EXTRAS -> MATCH

class Bateria:
    """Va a representar la bateria del coche electrico"""

    def __init__(self, capacidad, tipo_pila, num_pilas, peso):
        """Inicializar los argumentos 
        Capacidad = int
        Tipo_pila = int
        Num_pilas = int
        Peso = int
        """
        self._capacidad = capacidad
        self._tipo_pila = tipo_pila
        self._num_pilas = num_pilas
        self._peso = peso

    def especificaciones_bateria(self):
        """Imprimir las especificaciones de la bateria"""
        print(f"Capacidad: {self._capacidad} KWh \
              \nTipo de pilas: {self._tipo_pila}\
              \nNúmero de pilas: {self._num_pilas}\
              \nPeso de la bateria: {self._peso} kg")

bateria_tesla_modelS = Bateria(300, 2170, 203_136, 480)
tesla_modelS = CocheElectrico("Tesla", "Model S", 360, 280, 15, bateria_tesla_modelS)

tesla_modelS.especificaciones()
tesla_modelS.detalles_bateria()

