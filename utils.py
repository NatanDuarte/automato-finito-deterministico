green = '\033[32m'
yellow = '\033[33m'
blank = '\33[0m'


def print_affirmative(phrase: str) -> None:
    print(green+f'\nA frase "{phrase}" foi reconhecida pelo autômato.')

def print_negative(phrase: str) -> None:
    print(yellow+f'\nA frase "{phrase}" não foi reconhecida pelo autômato.')
