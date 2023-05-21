import string

def get_alphabet_letters() -> str:
    alphabet = list(string.ascii_lowercase)
    alphabet.append(' ')
    return alphabet

states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8']

start_state = 'q0'

accept_states = ['q8']

transitions = {
    'q0': {'o': 'q1', 'e': 'q7', ' ': 'q0', 'a': 'q1'},
    'q1': {'s': 'q2', ' ': 'q1', 'm': 'q4', 'c': 'q0'},
    'q2': {'a': 'q3', ' ': 'q2'},
    'q3': {'b': 'q6', ' ': 'q3', 'u': 'q8'},
    'q4': {'e': 'q5', ' ': 'q4', 'p': 'q7'},
    'q5': {'b': 'q0', ' ': 'q5', 'n': 'q6'},
    'q6': {'i': 'q7', 'e': 'q5', ' ': 'q6'},
    'q7': {'u': 'q8', 'o': 'q3', ' ': 'q7', 'n': 'q0', 'r': 'q7'},
    'q8': {' ': 'q8', 'c': 'q8', 'e': 'q8', 'r': 'q8', 'v': 'q8', 'j': 'q8', 'a': 'q8', 's': 'q8', 'l': 'q8', 'd': 'q8' }
}

input_phrases = [
    "O sábio bebeu cerveja",
    "A menina comprou salada",
]