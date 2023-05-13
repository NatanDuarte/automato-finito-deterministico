from automatoFinitoDeterministico import AutomatoFinitoDeterministico

automato = AutomatoFinitoDeterministico(
    states=['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'],
    alphabet=['o', 's', 'á', 'b', 'e', 'i', 'u', 'c', 'r', 'v', 'j', 'a', ' '],
    start_state='q0',
    accept_states=['q8'],
    transitions={
        'q0': {'o': 'q1', 'e': 'q7', ' ': 'q0'},
        'q1': {'s': 'q2', ' ': 'q1'},
        'q2': {'á': 'q3', ' ': 'q2'},
        'q3': {'b': 'q6', ' ': 'q3'},
        'q4': {'e': 'q5', ' ': 'q4'},
        'q5': {'b': 'q0', ' ': 'q5'},
        'q6': {'i': 'q7', 'e': 'q5', ' ': 'q6'},
        'q7': {'u': 'q8', 'o': 'q3', ' ': 'q7'},
        'q8': {' ': 'q8', 'c': 'q8', 'e': 'q8', 'r': 'q8', 'v': 'q8', 'j': 'q8', 'a': 'q8'}
    }
)

frase = "O sábio bebeu cerveja"

if automato.run(frase):
    print(f'A frase "{frase}" foi reconhecida pelo autômato.')
else:
    print(f'A frase "{frase}" não foi reconhecida pelo autômato.')