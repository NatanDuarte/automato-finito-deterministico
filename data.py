import string

def get_alphabet_letters() -> str:
    # alphabet.append(' ')
    #alphabet = list(string.ascii_lowercase)
    alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u','v', 'z']
    return alphabet

states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8']

start_state = 'q0'

accept_states = ['q8']

transitions = {
    'q0': {'o': 'q1', 'e': 'q7', ' ': 'q0', 'a': 'q1', 'g': 'q0', 'd': 'q0', 'h': 'q7'},
    'q1': {'s': 'q2', ' ': 'q1', 'm': 'q4', 'c': 'q0','z': 'q6', 'a': 'q7'}, 
    'q2': {'a': 'q3', ' ': 'q2', 't': 'q2'},
    'q3': {'b': 'q6', ' ': 'q3', 'u': 'q8', 'r': 'q6', 'p': 'q3'},
    'q4': {'e': 'q5', ' ': 'q4', 'p': 'q7', 'a': 'q1'},
    'q5': {'b': 'q0', ' ': 'q5', 'n': 'q6', 's': 'q8', 'p': 'q8'},
    'q6': {'i': 'q7', 'e': 'q5', ' ': 'q6', 'g': 'q8'},
    'q7': {'u': 'q8', 'o': 'q3', ' ': 'q7', 'n': 'q0', 'r': 'q7', 'a': 'q0', 'e': 'q8', 'l': 'q6'},
    'q8': {' ': 'q8', 'c': 'q8', 'e': 'q8', 'r': 'q8', 'v': 'q8', 'j': 'q8', 'a': 'q8', 's': 'q8', 'l': 'q8', 'd': 'q8','u': 'q1', 'i': 'q7', 'o': 'q8' }
}

input_phrases = [
    "O sábio bebeu cerveja",
    "A menina comprou salada",
    "Gostaria de reservar uma mesa",
    "O cozinheiro preparou algo"
]

artigo = {'o', 'a', 'uma'}
preposi = {'de'}
verbs = {'beb', 'compr', 'reserv', 'prepar', 'gost'}
subs = {'cervej', 'sal', 'mes', 'sab', 'menin', 'cozinheir'}
pronom = {'algo'}



states2 = ['q0', 'q1', 'q2', 'q3', 'q4']

start_state2 = 'q0'

accept_states2 = ['q3']

transitions2 = {
    'q0': {'verbs': 'q2', 'art': 'q1'},
    'q1': {'subs': 'q3'}, 
    'q2': {'prepo': 'q4', 'art': 'q1', 'subs': 'q3', 'pronom': 'q3'},
    'q3': {'verbs': 'q2'},
    'q4': {'verbs': 'q2'}
}

classificacoes = {
    'artigo': ['o', 'a', 'uma'],
    'preposisoes': ['de'],
    'verbos': ['beb', 'compr', 'reserv', 'prepar', 'gost'],
    'subs': ['cervej', 'sal', 'mes', 'sabi', 'menin', 'cozinheir'],
    'pronom': ['algo']
}
