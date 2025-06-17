def guess_word(secret_word, test_letter, attempt_word):
    """
    Checkea si la letra está en sevret word y si la palabra es igual
    ARG: secret_word = Palabra secreta
    test_letter = Letra a verificar que se encuentra en secret word
    attempt_word = Palbra que debe ser igual que secret word
    ---
    Return:
    Print: La letra 'X' está en la palbra Secret Word
    Print: La palabra 'XXX' es igual que Secret Word
    """
    letter_in_word = test_letter in secret_word
    print("¿La letra de prueba se encuentra en la palabra?", letter_in_word)
    result = (attempt_word == secret_word) and (len(attempt_word) == len(secret_word))
    print("El jugador gana:", result)

def main():
    print("=== Letter and Word Guessing Game ===")
    secret_word = input("Introduce secret word: ")
    test_letter = input("Intoduce test_letter: ")
    attempt_word = input("Introduce attempt_word: ")
    guess_word(secret_word, test_letter, attempt_word)

if __name__ == "__main__":
    main()