import sys

def rectangle(x, y, z):
    """
    Print a rectangle of characters (x = wide, y = high) on the screen:

    For syle A:
    - 'o' in the corners
    - '-' in the horizontal edges
    - '|' in the vertical edges
    - ' ' spaces inside

    For style B:
    - 'B' in the corners
    - '/' in the horizontal and vertical edges
    - ' ' spaces inside

    For style C:
    - 'O' in the corners
    - 'xAAAAx' in the horizontal edges, depends on wide.
    - 'x' in the vertical edges
    - 'OBBBO' inside the rectangle
    """
    fila = ""
    i = 0
    j = 0

    # Style A
    if (z == 'A'):
        corner = "o"
        horizontal_edge = "-"
        vertical_edge = "|"
        space = " "

    # Style B
    if (z == 'B'):
        corner = "B"
        horizontal_edge = "/"
        vertical_edge = "/"
        space = " "
    
    if ((x<1) or (y<1)):
        return
    else:
        if (z == 'A' or z == 'B'):
            while (j<y):
                if (j == 0) or (j == y-1):
                    while (i<x):
                        if (i == 0) or (i == x-1):
                            fila += corner
                        else:
                            fila += horizontal_edge
                        i += 1
                    print(fila)
                    fila = ""
                    i = 0
                else:
                    while (i<x):
                        if (i == 0) or (i == x-1):
                            fila += vertical_edge
                        else:
                            fila += space
                        i += 1
                    print(fila)
                    fila = ""
                    i = 0
                j += 1
    # Style C
        elif(z == 'C'):
            corner = "O"
            horizontal_edge = "A"
            vertical_edge = "x"

            if ((x<1) or (y<1)):
                return
            else:
                while (j<y):
                    if (j == 0) or (j == y-1):
                        while (i<x):
                            if (i == 0) or (i == x-1):
                                fila += corner
                            elif (i == 1) or (i == x-2):
                                fila += "x"
                            else:
                                fila += horizontal_edge
                            i += 1
                        print(fila)
                        fila = ""
                        i = 0
                    else:
                        while (i<x):
                            if (i == 0) or (i == x-1):
                                fila += vertical_edge
                            elif (i == 1) or (i == x-2):
                                fila += "O"
                            else:
                                fila += "B"
                            i += 1
                        print(fila)
                        fila = ""
                        i = 0
                    j += 1           
  
def main():
    if len(sys.argv) == 4:
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            z = str(sys.argv[3])
            rectangle(x, y, z)
            if z not in ['A', 'B','C']:
                raise ValueError
        except ValueError:
            print("Los dos primeros argumentos deben ser números enteros y el tercero puede ser 'A','B' o 'C'")
    else:
        print("Uso: python desafio.py <ancho> <alto> <estilo>")

if __name__ == "__main__":
    main()

