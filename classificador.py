from data2 import classificacoes

class Classifier:
    def __init__(self, states:list, tokens:list,
                 start_state:str, accept_states:list, transitions:dict) -> None:
        self.states = states
        self.tokens = tokens
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

    def classify(self):
        current_state = self.start_state
        classe = None
        intention = None
        for token in self.tokens:
            if token in classificacoes['artigo']:
                classe = 'art'
            elif token in classificacoes['preposisoes']:
                classe = 'prepo'
            elif token in classificacoes['subs']:
                classe = 'subs'
            elif token in classificacoes['verbos']:
                classe = 'verbs'
            elif token in classificacoes['pronom']:
                classe = 'pronom'

            if (self._is_valid_state(current_state) or
                self._contains_valid_transition(current_state, classe)):
                return False, classe
            if token in classificacoes['verbos']:
                if token == 'beb':
                    intention = 'beber'
                elif token == 'compr':
                    intention = 'comprar'
                elif token == 'reserv': 
                    intention = 'reservar'
                elif token == 'prepar':
                    intention = 'preparar'
                elif token == 'gost':
                    intention = 'gostar'
            current_state = self.transitions[current_state][classe]
        return current_state in self.accept_states, intention

    def _contains_valid_transition(self, current_state:str, symbol) -> bool:
        return symbol not in self.transitions[current_state]

    def _is_valid_state(self, current_state) -> bool:
        return current_state not in self.transitions