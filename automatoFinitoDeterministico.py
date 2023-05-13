class AutomatoFinitoDeterministico:
    def __init__(self, states:list, alphabet:list, 
                 start_state:str, accept_states:list, transitions:dict):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

    def run(self, input_string:str):
        current_state = self.start_state
        for symbol in input_string.lower():
            if symbol not in self.alphabet:
                return False
            if current_state not in self.transitions or symbol not in self.transitions[current_state]:
                return False
            current_state = self.transitions[current_state][symbol]
        return current_state in self.accept_states
