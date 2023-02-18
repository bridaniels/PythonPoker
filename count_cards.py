# Counting Cards 

'''
IMPORT PLAY_POKER.PY EVENTUALLY AND CLEAN UP 
'''
SUITES = ['Heart', 'Diamond', 'Spade', 'Club']
NUMVAL = [2,3,4,5,6,7,8,9,10,11,12,13,14]
FACECARDS = {
    "J": 11, 
    "Q": 12, 
    "K": 13, 
    "A": 14, 
    11: "J", 
    12: "Q", 
    13: "K", 
    14: "A"
}
# Define Classes
class Card: 
    def __init__(self, numval, suit): 
        self.numval = numval
        self.suit = suit
class Player: 
    def __init__(self, id, name, cards, points=0): 
        self.id = id 
        self.name = name 
        self.cards = cards
        self.points = points 
# Create Deck 
def initialize_deck_facecards(): 
    starting_deck = []
    for numval in NUMVAL: 
        for suit in SUITES: 
            if numval in FACECARDS: 
                c = Card(FACECARDS[numval], suit)
            else: 
                c = Card(numval,suit)
            starting_deck.append(c)
    return starting_deck
def initialize_deck_one_liner():
    starting_deck = [Card(numval,suit) for numval in NUMVAL for suit in SUITES]
    return starting_deck
'''
END OF PLAY_POKER.PY 
'''

# HI-LOW CARD COUNTING STRATEGY 
