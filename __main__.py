from DeterministicFiniteAutomaton import DeterministicFiniteAutomaton
from classificador import Classifier

from utils import *
from data import *
from data2 import *

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

            classifier = Classifier(
                start_state=start_state2,
                accept_states=accept_states2,
                states=states2,
                tokens=tokens,
                transitions=transitions2
            )

            recognized,  intencao = classifier.classify()

            print(recognized, intencao)
    except Exception as e:
        print(f'Erro ao executar fluxo:\n{e.__traceback__}')

if __name__ == '__main__':
    main()
