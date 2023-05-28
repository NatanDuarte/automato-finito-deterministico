
states2 = ['q0', 'q1', 'q2', 'q3', 'q4']

start_state2 = 'q0'

accept_states2 = ['q3']

transitions2 = {
    'q0': {'verbs': 'q2', 'art': 'q1'},
    'q1': {'subs': 'q3'}, 
    'q2': {'prepo': 'q4', 'art': 'q1', 'subs': 'q3'},
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
