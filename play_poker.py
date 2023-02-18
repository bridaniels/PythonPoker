# Texas Hold'em Poker
# OOP

# Import Libraries 
import random 

# Basic Setup
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
num_players = 5

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

'''
Random Card Dealer Work
'''
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
# Randomly Deal Cards 
def deal_cards_random(cards): 
    i = random.randint(0, len(cards)-1)
    card = cards[i]
    cards.pop(i)
    return card, cards   
# Deal Hole Cards 
def hole_cards(cards, num_opp): 
    opp_hands = []
    for _ in range(num_opp-1): 
        card1, cards = deal_cards_random(cards)
        card2, cards = deal_cards_random(cards)
        opp_hands.append([card1,card2])
    card1, cards = deal_cards_random(cards)
    card2, cards = deal_cards_random(cards)
    your_hand = [card1, card2]
    return your_hand, opp_hands
# The Flop 
def the_flop(cards): 
    burnt_1, cards = deal_cards_random(cards)
    burnt_card = [burnt_1]
    c1, cards = deal_cards_random(cards)
    c2, cards = deal_cards_random(cards)
    c3, cards = deal_cards_random(cards)
    community_cards = [c1,c2,c3]
    return burnt_card, community_cards
# Turn or River 
def turn_river(cards): 
    burnt, cards = deal_cards_random(cards)
    c1, cards = deal_cards_random(cards)
    return burnt, c1 

'''
Player Card Analysis 
'''
# GET
def get_card_values(cards): 
    cardValues = []
    for c in cards: 
        cardValues.append(int(c.numval))
    return cardValues
def get_highest_card(cardValues): 
    return max(cardValues)
def get_royal_cards(val): 
    if val == 1 or val == 14: 
        return "A"
    elif val == 13:
        return "K"
    elif val == 12: 
        return "Q"
    elif val == 11: 
        return "J"
    else: 
        return str(val)  
def get_best_5(cards): 
    cardValues = get_card_values(cards)
    cardValues.sort(reverse=True)
    return cardValues[:5]
# IS?
def is_ace(cardValue): 
    if cardValue == 14 or cardValue == 1: 
        return True
    return False 


'''
Player Hand Analysis 
'''
# ROYAL FLUSH

# STRAIGHT FLUSH

# FOUR-OF-A-KIND

# FULL HOUSE 

# FLUSH

# STRAIGHT

# THREE-OF-A-KIND 

# TWO-PAIR

# ONE-PAIR 

# HIGH CARD 

