# Poker Cards 


# Basic Card Details to Build the Deck 
SUITES = ['Heart', 'Diamond', 'Spade', 'Club']
NUMVAL = [2,3,4,5,6,7,8,9,10,11,12,13,14]

RANKS = {
        'Royal Flush': 900,
        'StraightFlush': 800,
        'FourKind': 700,
        'FullHouse': 600,
        'Flush': 500,
        'Straight': 400, 
        'ThreeKind': 300, 
        'TwoPairs': 200, 
        'Pair': 100, 
        'High': 0
        }

# Define the card 
class Card: 
    def __init__(self, numval, suite): 
        self.numval = numval
        self.suite = suite 


# Define the Player 
class Player: 
    def __init__(self, id, name, cards, points=0):
        self.id = id 
        self.name = name 
        self.cards = cards 
        self.points = points 

'''
FUNCTIONS FOR THE DECK
'''
# GET
def get_new_deck(): 
    deck = [Card(numval,suite) for numval in range(1,14) for suite in SUITES]
    return deck 
def get_card_values(cards): 
    cardValues = []
    for c in cards: 
        cardValues.append(int(c.numval))
    return cardValues
def get_highest_card(cardValues): 
    return max(cardValues)

# IS? 
def is_card_ace(cardValue): 
    if cardValue ==14 or cardValue ==1: 
        return True
    return False
def is_straight_flush_possible(cards): 
    if is_straight_flush_possible(cards)[0] and is_straight_flush_possible(cards)[0]: 
        ls1 = []
        ls2 = []
        for c in cards: 
            ls1.append(str(c.numval) + c.suite)

        for c in ls1: 
            # HEART 
            if c[-1] == 'Heart':
                uniqueNum = int(c[:-1]) + 0 
                ls2.append(uniqueNum)
                if is_card_ace(c[:-1]): 
                    ls2.append(1 + 0)
            # DIAMOND
            elif c[-1] == 'Diamond':
                uniqueNum = int(c[:-1]) + 13
                ls2.append(uniqueNum) 
                if is_card_ace(c[:-1]): 
                    ls2.append(1 + 13) 
            # SPADES
            elif c[-1] == 'Spades': 
                uniqueNum = int(c[:-1]) + 26
                ls2.append(uniqueNum) 
                if is_card_ace(c[:-1]): 
                    ls2.append(1 + 26) 
            # CLUBS
            else: 
                uniqueNum = int(c[:-1]) + 39 
                ls2.append(uniqueNum) 
                if is_card_ace(c[:-1]): 
                    ls2.append(1 + 39)
        
        ls2.sort(reverse=True)

        isPossible, val = is_straight_flush_possible(ls2, True) 
        if isPossible: 
            return True, val % 13
    
    return False, 0  
def is_four_possible(cards): 
    cardValues = get_card_values(cards)
    found = False
    num = 1 
    for i in range(4): 
        sameCount = cardValues.count(cardValues[i])
        if sameCount == 4: 
            found = True
            num = cardValues[i]
    if found: 
        cardValues.remove(num)
        cardValues.remove(num)
        cardValues.remove(num)
        cardValues.remove(num) 
        cardValues.sort(reverse=True)
        return True, [num, get_highest_card(cardValues)]
    return False, 0
def is_full_house_possible(cards): 
    cardValues = get_card_values(cards)
    cardValues.sort(reverse=True)
    fullHouseCards = []

    for i in range(4): 
        sameCount = cardValues.count(cardValues[i])
        if sameCount == 3: 
            fullHouseCards.append(cardValues[i])
            break 
    if len(fullHouseCards) == 1: 
        cardValues.remove(fullHouseCards[0])
        cardValues.remove(fullHouseCards[0])
        cardValues.remove(fullHouseCards[0])
        for i in range(3): 
            sameCount = cardValues.count(cardValues[i])
            if sameCount == 2: 
                fullHouseCards.append(cardValues[i])
                break 
    if len(fullHouseCards) == 2: 
        return True, fullHouseCards
    
    return False, 0 






'''
working on above 
'''