

def swap_int(a, b):
    """
    Intercambia el contenido y las direcciones de memoria de dos enteros
    """
    id_a = id(a)
    id_b = id(b)

    print("\nValores al inicio:")
    print(f"Número a = {a} | Dirección en memoria = {id_a}")
    print(f"Número b = {b} | Dirección en memoria = {id_b}")
    
    temp = id(a) # temp = valor temporal
    id_a = id(b)
    id_b = temp

    temp = a
    a = b
    b = temp

    print("\nValores intercambiados:")
    print(f"Número a = {a} | Dirección en memoria = {id_a}")
    print(f"Número b = {b} | Dirección en memoria = {id_b}")

def main():
    try: 
        a = int(input("Introduce el primer número entero: "))
        b = int(input("Introduce el segundo número entero: "))
        swap_int(a,b)
    except ValueError:
        print("ERROR: Tienen que ser números enteros")
    

if __name__ == "__main__":
    main()