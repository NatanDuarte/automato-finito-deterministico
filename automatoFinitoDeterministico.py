import unicodedata

from nltk.stem import PorterStemmer


class AutomatoFinitoDeterministico:
    def __init__(self, states:list, alphabet:list, 
                 start_state:str, accept_states:list, transitions:dict) -> None:
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

    def recognize(self, phrase:str) -> bool:
        current_state = self.start_state
        for symbol in phrase:
            if symbol not in self.alphabet:
                return False
            if (self._is_valid_state(current_state) or
                self._contains_valid_transition(current_state, symbol)):
                return False
            current_state = self.transitions[current_state][symbol]
        return current_state in self.accept_states

    def format_phrase(self, phrase:str) -> str:
        stemmer = PorterStemmer()
        phrase = unicodedata.normalize('NFKD', phrase).encode('ASCII', 'ignore').decode('utf-8')
        return ' '.join([stemmer.stem(word) for word in phrase.split(' ')]).lower().strip()

    def _contains_valid_transition(self, current_state:str, symbol) -> bool:
        return symbol not in self.transitions[current_state]

    def _is_valid_state(self, current_state) -> bool:
        return current_state not in self.transitions
