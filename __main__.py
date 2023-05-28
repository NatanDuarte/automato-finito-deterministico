from DeterministicFiniteAutomaton import DeterministicFiniteAutomaton
from classificador import Classifier

from utils import *
from data import *
import os


green = '\033[32m'
yellow = '\033[33m'
blank = '\33[0m'


def main():
    automaton = DeterministicFiniteAutomaton(
        states,
        get_alphabet_letters(),
        start_state,
        accept_states,
        transitions
    )

    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        for phrase in input_phrases:
            phrase = automaton.format_phrase(phrase)
            recognized = automaton.recognize(phrase)

            print_affirmative(phrase) if recognized else print_negative(phrase) 

            if recognized:
                tokens = automaton.applyStemmer(phrase)
                print(blank+f"\ntokens: {tokens}")

                classifier = Classifier(
                    start_state=start_state2,
                    accept_states=accept_states2,
                    states=states2,
                    tokens=tokens,
                    transitions=transitions2
                )

                recognized,  intencao = classifier.classify()

                if recognized:
                    print(green+f'intenção reconhecida: {intencao}')
                else:
                    print(yellow+f'nao reconhecido')

                print(blank+f'------------------------------------------------------------------')
    except Exception as e:
        print(yellow+f'Erro ao executar fluxo:\n{e.__traceback__}')

if __name__ == '__main__':
    main()
