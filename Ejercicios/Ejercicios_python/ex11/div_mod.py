import sys

def div_mod(a, b, c):
    """
    Divide los dos parámetros a y b y luego le aplica un módulo de c
    """
    print(f"({a}/{b}) % {c} = {a/b} % {c} = {(a/b)%c}")
    


def main():
    if (len(sys.argv) == 4):
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            c = int(sys.argv[3])
            if b == 0:
                print("ERROR: No se puede dividir entre 0.")
            else:
                div_mod(a,b,c)
        except ValueError:
            print("ERROR: Los argumentos han de ser números enteros.")
    else:
        print("Uso: python div_mod.py <num1> <num2> <num3>")	


if __name__ == "__main__":
    main()