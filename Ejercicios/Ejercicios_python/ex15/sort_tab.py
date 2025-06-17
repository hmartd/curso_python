import string

def sort_tab(array):
    """
    Ordena el array en orden ascendente
    """
    array.sort()
    print("Array ordenado: ", array) 

def main():
    n = int(input("¿De cuántos elementos quieres el array? "))
    i = 0
    result = []
    while (i < n):
        digit = int(input(f"Introduce el elemento n{i+1}  del array: "))
        result = result + [digit]
        i += 1
    
    sort_tab(result)
    

if __name__ == "__main__":
    main()