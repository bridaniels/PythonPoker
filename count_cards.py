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
def initialize_deck_one_liner():
    starting_deck = [Card(numval,suit) for numval in NUMVAL for suit in SUITES]
    return starting_deck
# GET
def get_card_values(cards): 
    cardValues = []
    for c in cards: 
        cardValues.append(int(c.numval))
    return cardValues
'''
END OF PLAY_POKER.PY 
'''

# HI-LOW CARD COUNTING STRATEGY 
count_val = {
    2: 1,
    3: 1,
    4: 1, 
    5: 1, 
    6: 1, 
    7: 0,
    8: 0,
    9: 0,
    10: -1,
    'J': -1,
    'Q': -1,
    'K': -1,
    'A': -1, 
    11: -1,
    12: -1,
    13: -1,
    14: -1
}
def count_cards(hand): 
    return sum(count_val[i] for i in hand)
