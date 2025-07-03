# Aquí irá la clase EstacionClimatica
import numpy as np
import matplotlib as plt

class EstacionClimatica:
    def __init__(self, nombre, temperaturas=None):
        """Inicializa los atributos
        Argumentos:
        nombre - string con el nombre de la estacion climática"""

        self._nombre = nombre
        self._temperaturas = np.random.randint(15, 35, 30) # Genera un array con temperaturas aleatorias entre 15 y 35ºC para 30 días.
 
    def media(self):
        """Calcula la temperatura media"""
        return round(np.mean(self._temperaturas), 2) # Redondeamos a 2 decimales con round() la media

    def maxima(self):
        """Calcula la temperatura máxima"""
        return np.max(self._temperaturas)

    def minima(self):
        """Calcula la temperatura mínima"""
        return np.min(self._temperaturas)

    def resumen(self):
        """Devuelve un diccionario con Media, Máxima y Mínima"""
        diccionario = {"Media": float(self.media()),
                       "Máxima": int(self.maxima()),
                       "Mínima": int(self.minima())}
        print(diccionario)
       

