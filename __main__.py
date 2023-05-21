from DeterministicFiniteAutomaton import DeterministicFiniteAutomaton

from utils import *
from data import *


def main():
    automaton = DeterministicFiniteAutomaton(
        states,
        get_alphabet_letters(),
        start_state,
        accept_states,
        transitions
    )

    print('\n')
    try:
        for phrase in input_phrases:
            phrase = automaton.format_phrase(phrase)
            recognized = automaton.recognize(phrase)

            print_affirmative(phrase) if recognized else print_negative(phrase) 

            tokens = automaton.applyStemmer(phrase)
            print(f'tokens: {tokens}')

            # TODO: reconhecer intenção
    except Exception as e:
        print(f'Erro ao executar fluxo:\n{e}')

if __name__ == '__main__':
    main()
