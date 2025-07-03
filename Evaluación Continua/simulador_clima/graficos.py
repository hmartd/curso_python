# Aquí irán las funciones de visualización con Matplotlib
import matplotlib.pyplot as plt
import clima

def graficar_temperaturas(estacion):
    """Muestra un gráfico de líneas con las temperaturas por día"""
    x = list(range(1, 31)) # variable independiente 
    y = estacion._temperaturas # variable dependiente

    plt.title(f"Clima en {estacion._nombre}")
    plt.plot(x, y, label = estacion._nombre) # Se añade la etiqueta con el nombre de la estación

    # Nombre ejes
    plt.xlabel("Días")
    plt.ylabel("Temperatura (°C)")

    plt.legend()
    plt.show()


def comparar_estaciones(lista_estaciones):
    """Muestra un gráfico donde se comparan todas las curvas de temperatura"""
    
    x = list(range(1, 31)) # variable independiente 
    
    for estacion in lista_estaciones:
        y = estacion._temperaturas # variable dependiente
        plt.plot(x, y, label = estacion._nombre) # Se añade la etiqueta con el nombre de la estación

    # Nombrar título y ejes 
    plt.title("Comparación del clima")
    plt.xlabel("Días")
    plt.ylabel("Temperatura (°C)")

    plt.legend(loc = 'upper right', fontsize = 8)
    plt.show()
        


bcn = clima.EstacionClimatica("Barcelona")
md = clima.EstacionClimatica("Madrid")
pa = clima.EstacionClimatica("París")
ny = clima.EstacionClimatica("Nueva York")

lista = [bcn, md, pa, ny]
#graficar_temperaturas(bcn)
comparar_estaciones(lista)