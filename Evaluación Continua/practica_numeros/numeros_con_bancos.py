"""
Objetivo: Crear un simulador de cuota mensual de préstamos hipotecarios

1. Crea una clase llamada LoanSimulator 
que modele el proceso de calcular el pago total de un préstamo hipotecario, 
incluyendo tanto el capital inicial como los intereses generados 
a lo largo del plazo del préstamo.

2. La clase toma como parámetros detalles_prestamo, 
un número complejo cuya parte real será la entrada proporcionada 
para la hipoteca y la parte imaginaria el tipo de interés.

3. También tomará como parámetro opcional los años del préstamos hipotecario (por defecto 30) 
y el precio de la vivienda (por defecto para este ejercicio 300_000).

4. Deben almacenarse en el método constructor de la clase al menos los siguientes atributos de instancia:
4.1 tasa_mensual: Tasa de interés (parte imaginaria de detalles_prestamo) dividida entre 12 para convertirla a mensual y dividida entre 100
4.2 numero_pagos: Numero de pagos totales (número de años * 12).
4.3 entrada: Parte real del parámetro detalles_prestamo.
4.4 prestamo: Precio de la vivienda restando la entrada.
4.5 cuota_mensual: Parámetro a calcular en el programa (inicialmente 0).

5. Implementa un método llamado calcular_pago_total que realice 
el cálculo de la cuota mensual a pagar del préstamo hipotecario 
y que actualice el atributo cuota_mensual. 
El cálculo de la cuota mensual se realiza mediante la siguiente fórmula:
Cuota mensual = prestamo * (tasa de interés mensual * (1 + tasa de interés mensual)**número de pagos) / ((1 + tasa de interés mensual)**número de pagos - 1)

6. Implementa otro método mostrar_resultados que imprima la simulación de la hipoteca: 
el precio de la vivienda, la entrada, los años y finalmente la cuota mensual.

7. Instancia la clase con un número complejo representativo y ejecuta los métodos para calcular el pago total y mostrar los resultados.
"""

"""
Resultado esperado
----- Simulación Hipoteca -----
Para una vivienda de 300000 euros, aportando una entrada de 50000.0 euros y con una tasa de interés del 2.5% anual durante 30 años:
Cuota mensual a pagar: 987.8022470442972 euros
----- Fin de la Simulación -----
"""


class LoanSimulator:
    """Esta es una clase que representa un simulador de préstamos"""

    def __init__(self, detalles_prestamo, años=30, precio_vivienda=300000): # si no se introduce nada, por defecto se estable años = 30 y precio_vivienda=300_000
        """Inicializa la instancia con los detalles del préstamo, duración y precio
        
        Args:
        detalles_prestamo (Complex): 
            Parte Real = Capital inicial del préstamo | Parte imaginaria = Tasa de interés
        años (int, opcional): Duración del préstamo (Por defecto 30 años)
        precio_vivienda (int, opcional): Precio total de la vivienda (Por defecto 300.000 €)"""

        self._tasa_interes = detalles_prestamo.imag # Tasa de interés del prestamo
        self._entrada = detalles_prestamo.real # Entrada aportada por el cliente
        self._años = años # Años del préstamo
        self._precio_vivienda = precio_vivienda # Precio de la vivienda
        #----------------------#
        self._tasa_mensual = (self._tasa_interes / 12) / 100 # Tasa de interés anual => Mensual
        self._numero_pagos = (self._años * 12) # Duración del préstamo en meses
        self._prestamo = self._precio_vivienda - self._entrada # Préstamo de la vivienda
        self._cuota_mensual = 0 # Simulación de la cuota mensual

    
    def calcular_pago_total(self):
        """Calcula la cuota mensual del préstamo según la tasa de interés y número de pagos"""
        self._cuota_mensual = self._prestamo * (self._tasa_mensual * (1 + self._tasa_mensual)**self._numero_pagos) / ((1 + self._tasa_mensual)**self._numero_pagos - 1)
    
    def mostrar_resultados(self):
        """
        Imprime los resultados de la simulación de la hipoteca (Precio Vivienda, Entrada, Tasa de interés, Duración y Cuota mensual)
        """
        print(f"----- Simulación Hipoteca -----\nPara una vivienda de {self._precio_vivienda}€, aportando una entrada de {self._entrada}€ y con una tasa de interés del {self._tasa_interes}% anual durante {self._años} años:\nCuota mensual a pagar: {self._cuota_mensual} euros\n----- Fin de la Simulación -----")
        


# Bancos "BBVA, CAIXABANK, SABADELL, SANTANDER"
# SUBCLASES

class Bbva(LoanSimulator):
    def __init__(self, entrada, años = 30, precio_vivienda = 300_000):
        self._tasa_interes = 2.5j
        self._detalles_prestamo = entrada + self._tasa_interes
        super().__init__(self._detalles_prestamo, años, precio_vivienda)

class CaixaBank(LoanSimulator):
    def __init__(self, entrada, años = 30, precio_vivienda = 300_000):
        self._tasa_interes = 2.74j
        self._detalles_prestamo = entrada + self._tasa_interes
        super().__init__(self._detalles_prestamo, años, precio_vivienda)

class Sabadell(LoanSimulator):
    def __init__(self, entrada, años = 30, precio_vivienda = 300_000):
        self._tasa_interes = 2.69j
        self._detalles_prestamo = entrada + self._tasa_interes
        super().__init__(self._detalles_prestamo, años, precio_vivienda)

class Santander(LoanSimulator):
    def __init__(self, entrada, años = 30, precio_vivienda = 300_000):
        self._tasa_interes = 2.45j
        self._detalles_prestamo = entrada + self._tasa_interes
        super().__init__(self._detalles_prestamo, años, precio_vivienda)

entrada = 50_000 # Real = Entrada
años = 30
precio_vivienda = 300_000


# 1ra opción:

"""
loan_simulator = Bbva(entrada, años, precio_vivienda)
loan_simulator.calcular_pago_total()
loan_simulator.mostrar_resultados()

loan_simulator = CaixaBank(entrada, años, precio_vivienda)
loan_simulator.calcular_pago_total()
loan_simulator.mostrar_resultados()

loan_simulator = Sabadell(entrada, años, precio_vivienda)
loan_simulator.calcular_pago_total()
loan_simulator.mostrar_resultados()

loan_simulator = Santander(entrada, años, precio_vivienda)
loan_simulator.calcular_pago_total()
loan_simulator.mostrar_resultados()
"""


# 2a opción
for loan_simulator in [Bbva(entrada, años, precio_vivienda), 
                       CaixaBank(entrada, años, precio_vivienda), 
                       Sabadell(entrada, años, precio_vivienda), 
                       Santander(entrada, años, precio_vivienda)]:
    loan_simulator.calcular_pago_total()
    loan_simulator.mostrar_resultados()