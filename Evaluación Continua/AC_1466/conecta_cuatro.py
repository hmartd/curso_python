import random
import os
import platform

ROWS = 6
COLUMNS = 7

def clean_terminal():
    """Limpia la Terminal"""
    if platform.system() == "Windows": # En el caso de Windows
        os.system("cls")
    else:
        os.system("clear")

def create_board():
    """Crea un tablero vacío de 6x7"""
    matriz = []

    for fila in range(ROWS):
        matriz.append([]) # añade 6 filas
        for columna in range(COLUMNS):
            matriz[fila].append('.') # añade 7 columnas con '.'
    return matriz
        

def print_board(board):
    """Muestra el tablero por pantalla"""
    for num in range(7): # Imprime la cabecera
        if num != 6:
            print(num, end=" ") # si no es el último elemento imprime seguidos los números separados con un espacio
        else:
            print(num) # imprime el último elemento con salto de línea \n
    
    for fila in range(ROWS): # Imprime el tablero
        for columna in range(COLUMNS):
            if columna != 6:
                print(board[fila][columna], end=" ")
            else:
                print(board[fila][columna])    
    

def insert_piece(board, column, piece):
    """Inserta la ficha en la columna si es posible"""
    for row in reversed(range(ROWS)): # Esto es equivalente a range(ROWS, -1, -1)
        if board[row][column] == ".":
            board[row][column] = piece
            return True
    return False

def valid_column(board, column):
    """ Devuelve True si la columna es válida (entre 0 y 6 y no está llena)"""
    if column >= 0 and column <= COLUMNS-1:
        for fila in range(ROWS):
            if board[fila][column] == ".":
                return True
    return False          

def get_valid_columns(board):
    """
    Devuelve una lista de columnas válidas para jugar
    => Utiliza valid_column para filtrar las columnas disponibles
    """
    result = []

    for column in range(COLUMNS):
        if valid_column(board, column):
            result.append(column)
    return result

def full_board(board):
    """
    Devuelve True si el tablero está lleno
    => Comprueba si hay alguna columna con espacio
    """
    if get_valid_columns(board) == []:
        return True
    return False

def check_win(board, piece):
    """
    Devuelve True si hay 4 en raya de la ficha indicada
    => Comprueba horizontal, vertical y diagonales
    """
    # horizontal (-)
    for fila in range(ROWS): # recorre todas las filas
        for columna in range(COLUMNS - 3): # empieza desde la columna n0 hasta la n3 para que no haya desbordamiento
            if (board[fila][columna] == piece and
                board[fila][columna + 1] == piece and
                board[fila][columna + 2] == piece and
                board[fila][columna + 3] == piece):
                return True
    
    # vertical (|)
    for columna in range(COLUMNS): # recorre todas las columnas
        for fila in range(ROWS - 3): # empieza desde la fila n0 hasta la n2 para que no haya desbordamiento
            if(board[fila][columna] == piece and
               board[fila + 1][columna] == piece and
               board[fila + 2][columna] == piece and 
               board[fila + 3][columna] == piece):
                return True

    # diagonal (\)
    for fila in range(ROWS - 3): # empieza desde la fila n0 a la n2
        for columna in range(COLUMNS - 3): # empieza desde la columna n0 a la n3
            if (board[fila][columna] == piece and
                board[fila + 1][columna + 1] == piece and
                board[fila + 2][columna + 2] == piece and
                board[fila + 3][columna + 3] == piece):
                return True

    # diagonal (/)
    for fila in range(3, ROWS): # empieza desde la fila n3 hasta la última
        for columna in range(COLUMNS-3): # empieza desde la columna n0 hasta la n3
            if (board[fila][columna] == piece and
                board[fila - 1][columna + 1] == piece and
                board[fila - 2][columna + 2] == piece and
                board[fila - 3][columna + 3] == piece):
                return True

    return False
    

def cpu_easy(board):
    """
    Elige una columna aleatoria
    => Usa get_valid_columns() para elegir una columna
    """
    columns = get_valid_columns(board)
    return random.choice(columns)

def cpu_normal(board, cpu_piece, player_piece):
    """
    CPU que intenta ganar o bloquear al jugador
    => Implementa la lógica de ataque y defensa básica
    """
    pass

def cpu_hard(board, cpu_piece, player_piece):
    """
    CPU más avanzada: evalúa las mejores jugadas posibles
    => Implementa la puntuación de posiciones
    """
    best_positions = []
    for col in get_valid_columns(board):
        copia = [fila[:] for fila in board]
        insert_piece(copia, col, cpu_piece)
        if check_win(copia, cpu_piece):
            return col
        puntos = puntuacion_posicion(copia, cpu_piece) - puntuacion_posicion(copia, player_piece)
        best_positions.append((puntos, col))
    if best_positions:
        best_positions.sort(reverse=True)
        return best_positions[0][1]
    return cpu_easy(board)

def puntuacion_posicion(board, piece):
    """
    Evalúa cuán favorable es una posición para una ficha
    => Cuenta posibles líneas de 2, 3 o 4 en ventana
    """
    pass

def evaluar_ventana(window, piece):
    """
    Evalúa una ventana de 4 celdas
    => Retorna puntuación según cuántas fichas haya en la ventana
    """
    pass

def choose_difficulty(player_name):
    """Pide al usuario que elija dificultad"""
    while True:
        nivel = input(f"{player_name} elige la dificultad [easy] [normal] [hard]: ").strip().lower()
        if nivel in ["easy", "normal", "hard"]:
            return nivel
        print("=> [ERROR] Nivel incorrecto")

def choose_name():
    """Pide al usuario que elija su nombre"""
    nombre = input("Tu nombre: ")
    return nombre

def game():
    """Lógica principal del juego"""
    clean_terminal()
    board = create_board()
    player = "X"
    cpu = "0"
    player_name = choose_name()
    difficulty = choose_difficulty(player_name)
    shift = 0 # 
    finish = False

    while not finish:
        pass


if __name__ == "__main__":
    game()