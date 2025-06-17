import string

def inv_tab(array):
    """
    Invierte el array
    """
    print("Array: ", array)
    print("Array invertido: ", array[::-1]) 

def main():
    n = int(input("¿De cuántos elementos quieres el array? "))
    i = 0
    result = []
    while (i < n):
        digit = int(input(f"Introduce el elemento n{i+1}  del array: "))
        result = result + [digit]
        i += 1

    inv_tab(result)
    

if __name__ == "__main__":
    main()