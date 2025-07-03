# Aquí irá el flujo principal del programa

import clima
import graficos


def main():
    # Estaciones Climáticas
    bcn = clima.EstacionClimatica("Barcelona")
    md = clima.EstacionClimatica("Madrid")
    pa = clima.EstacionClimatica("París")
    ny = clima.EstacionClimatica("Nueva York")
    
    lista_estaciones = [bcn, md, pa, ny]
   
    print("============ RESUMEN ESTACIONES ============\n")
    for estacion in lista_estaciones:
        print(estacion._nombre.center(43))
        print("-"*43)
        estacion.resumen()
    
    graficos.comparar_estaciones(lista_estaciones)

    
    found = False
    while not found:
        respuesta = input("\n¿Quieres ver alguna ciudad en detalle? (si/no) ").strip()
        if respuesta.lower() == "si":
                ciudad = input("Nombre ciudad: ")
                for estacion in lista_estaciones:
                    if estacion._nombre == ciudad.title().strip():
                        graficos.graficar_temperaturas(estacion)
                        found = True
                if found == False:
                    print("Error => Has de elegir una ciudad válida.")
        elif respuesta.lower() == "no":
            return
        else:
            print("Error => Solo se puede introducir los valores (si/no)")



if __name__ == "__main__":
    main()


