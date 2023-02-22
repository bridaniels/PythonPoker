# Texas Hold'em Poker
# OOP

# Import Libraries 
import random 
import copy 

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
# Can't use Facecards with Certain Math
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
def get_players_hand(community,hole):
    player = copy.deepcopy(community)
    player.extend(hole)
    return player
def get_opponent_hands(community,opp_holes):
    opp_com = copy.deepcopy(community)
    x = [0] * len(opp_holes)
    for i in range(len(opp_holes)): 
        x[i] = opp_holes[i]
        x[i].extend(opp_com)
    return x 
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
Overall Hand Analysis 
'''
# FIND DUPLICATES 
def find_duplicates(cards): 
    numbers = [c.numval for c in cards]
    numbers.sort(reverse=True)
    dupes = [n for n in numbers if numbers.count(n) > 1]
    mult = len(dupes)
    
    # One Pair
    if mult == 2: 
        return "One_Pair"
    # Two Pair + Four of a Kind 
    elif mult == 4:
        if len(set(dupes)) == 2: 
            return "Two_Pair"
        elif len(set(dupes)) == 1: 
            return "Four_of_a_Kind"
    # Three of a Kind 
    elif mult == 3: 
        return "Three_of_a_Kind"
    # Full House
    elif mult == 5 and len(set(dupes)) == 2: 
        return "Full_House"
    # NOT ABOVE 
    else: 
        return "NO DUPLICATES: High Card"
# STRAIGHT/FLUSH/ROYAL
def is_straight_flush_royal(cards): 
    # SETUP
    suits = [c.suit for c in cards]
    values = [c.numval for c in cards]
    values = list(set(values))
    values.sort(reverse=True)
    if 14 in values: 
        values.append(1)
    # IS STRAIGHT/FLUSH/ROYAL
    def is_straight(values): 
        num_left = len(values)
        num_iter = num_left - 4
        if num_left > 4: 
            for i in range(num_iter):
                if values[i] - 1 == values[i+1]: 
                    if values[i+1] - 1 == values[i+2]:
                        if values[i+2] -1 == values[i+3]: 
                            if values[i+3] - 1 == values[i+4]:
                                return True
        return False
    def is_flush(suits):
        for i in range(len(suits)): 
            sameCount = suits.count(suits[i])
            if sameCount == 5:
                return True
        return False 
    def is_royal(values):
        royal = []
        for i in range(len(values)): 
            if values[i] >= 10:
                royal.append(values[i])
        if len(royal) == 5:
            return True
        return False 
    # ROUNDUP
    if is_straight(values) == True:
        if is_flush(suits) == True: 
            if is_royal(values) == True: 
                return "Royal_Flush"
            return "Straight_Flush"
        return "Straight"
    if is_flush(suits) == True: 
        return "Flush"
    return False

'''
Individual Hand Analysis 
'''
# ROYAL FLUSH
def is_royal_flush(cards):
    suits = [i.suit for i in cards]
    values = []
    # Straight Suit
    for i in range(len(suits)): 
        sameCount = suits.count(suits[i])
        if sameCount >= 5: 
            royal_suit = suits[i]
            # Check For Royals 
            for i in range(len(cards)):
                if cards[i].suit == royal_suit and cards[i].numval >= 10:
                    values.append(cards[i].numval)
                    values = list(set(values))
            if len(values) == 5: 
                return royal_suit, values, 100
    return "Royal Flush Error"

# STRAIGHT FLUSH
def is_straight_flush(cards):
    suits = [i.suit for i in cards]
    values = []
    # Straight Suit 
    for m in range(len(suits)): 
        sameCount = suits.count(suits[m])
        if sameCount >= 5: 
            flush_suit = suits[m]
            # Check For Consecutive 
            for n in range(len(cards)): 
                if cards[n].suit == flush_suit: 
                    values.append(cards[n].numval)
            if 14 in values:
                values.append(1) 
            values.sort(reverse=True)
            num_left = len(values)
            itr_num = num_left - 4
            if num_left > 4: 
                for i in range(itr_num):
                    if values[i] - 1 == values[i+1]: 
                        if values[i+1] - 1 == values[i+2]:
                            if values[i+2] - 1 == values[i+3]:
                                if values[i+3] - 1 == values[i+4]:
                                    return flush_suit, values, 90
    return "Straight Flush Error"

# FOUR-OF-A-KIND
def is_four_of_a_kind(cards): 
    values = [c.numval for c in cards]
    values.sort(reverse=True)
    best_hand = []
    for i in range(len(values)): 
        sumcount = values.count(values[i])
        if sumcount == 4:
            best_hand.append(values[i])
    for i in range(4):
        values.remove(best_hand[i])
    best_hand.append(values[0])
    values.remove(values[0])
    return best_hand, 80

# FULL HOUSE 
def is_full_house(cards): 
    numbers = [c.numval for c in cards]
    numbers.sort(reverse=True)
    triples = [n for n in numbers if numbers.count(n) > 2]
    doubles = [n for n in numbers if numbers.count(n) == 2]
    house = []
    if len(triples) == 3 or len(triples) == 6:
        for i in range(5):         
            house.append(triples[i])
    if len(house) == 3: 
        for i in range(2): 
            house.append(doubles[i])
    if len(house) == 5: 
        return house, 70
    return "Full House Error"

# FLUSH
def is_flush(cards):
    suits = [i.suit for i in cards]
    values = []
    for i in range(len(suits)): 
        sameCount = suits.count(suits[i])
        if sameCount == 5: 
            flush_suit = suits[i]
            # Pull Flush Cards
            for n in range(len(cards)): 
                if cards[n].suit == flush_suit: 
                    values.append(cards[n].numval)
            values.sort(reverse=True)
            return flush_suit, values[:5]
    return "Flush Error"

# STRAIGHT
def is_straight(cards): 
    values = [c.numval for c in cards]
    if 14 in values: 
        values.append(1)
    values = list(set(values))
    values.sort(reverse=True)
    numLeft = len(values)
    numIter = numLeft - 4
    if numLeft > 4: 
        for i in range(numIter): 
            if values[i] - 1 == values[i+1]: 
                if values[i+1] - 1 == values[i+2]:
                    if values[i+2] -1 == values[i+3]: 
                        if values[i+3] - 1 == values[i+4]:
                            if values[i+4] == 1: 
                                return values[-5:], max(values[-5:]),50
                            return values[:5], max(values[:5]), 50
    return "Straight Error"

# THREE-OF-A-KIND 
def is_three_of_a_kind(cards): 
    values = [c.numval for c in cards]
    values.sort(reverse=True)
    best_hand = []
    for i in range(len(values)): 
        sumcount = values.count(values[i])
        if sumcount == 3:
            best_hand.append(values[i])
    for i in range(3):
        values.remove(best_hand[i])
    best_hand.append(values[0])
    best_hand.append(values[1])
    values.remove(values[0])
    values.remove(values[1])
    return best_hand, 40

# TWO-PAIR
def is_two_pair(cards): 
    values = [c.numval for c in cards] 
    values.sort(reverse=True)
    dupes = [n for n in values if values.count(n) == 2]
    for i in range(4): 
        values.remove(dupes[i]) 
    dupes = dupes[:4]
    dupes.append(values[0])
    return dupes, 30

# ONE-PAIR 
def is_one_pair(cards): 
    numbers = [c.numval for c in cards]
    numbers.sort(reverse=True)
    dupes = [n for n in numbers if numbers.count(n) == 2]
    mult = len(dupes)
    if mult == 2: 
        numbers.remove(dupes[0])
        numbers.remove(dupes[1])
        dupes.append(numbers[0])
        return dupes, 20
    return "One Pair Error"

# HIGH CARD 
def is_high_card(cards):
    numbers = [c.numval for c in cards]
    numbers.sort()
    return numbers[-1], 10

'''
CHECKING
'''
def check_hand(cards, sfr_analysis, fd_analysis):
    # STRAIGHT FLUSH ROYAL + Find Duplicates Analysis 
    if sfr_analysis == "Royal_Flush":
        return is_royal_flush(cards)
    elif sfr_analysis == "Straight_Flush":
        return is_straight_flush(cards)
    elif fd_analysis == "Four_of_a_Kind":
        return is_four_of_a_kind(cards)
    elif fd_analysis == "Full_House":
        return is_full_house(cards)
    elif sfr_analysis == "Flush":
        return is_flush(cards)
    elif sfr_analysis == "Straight":
        return is_straight(cards)
    elif fd_analysis == "Three_of_a_Kind":
        return is_three_of_a_kind(cards)
    elif fd_analysis == "Two_Pair":
        return is_two_pair(cards)
    elif fd_analysis == "One_Pair":
        return is_one_pair(cards)
    else: 
        numbers = [c.numval for c in cards]
        numbers.sort()
        return numbers[-1], 10
'''
ANALYZE OPPONENTS HANDS
'''
def check_opponents(community,opp_hands): 
    hand = get_opponent_hands(community,opp_hands)
    k = len(hand)
    sfr,fd,check = [0]*k, [0]*k, [0]*k
    for i in range(k): 
        sfr[i] = is_straight_flush_royal(hand[i])
        fd[i] = find_duplicates(hand[i])
        check[i] = check_hand(hand[i],sfr[i],fd[i])
    return hand,sfr,fd,check

'''
WINNING HAND
'''
winning_hands = {
    100 : "Royal_Flush",
     90 : "Straight_Flush",
     80 : "Four_of_a_Kind", 
     70 : "Full_House", 
     60 : "Flush", 
     50 : "Straight", 
     40 : "Three_of_a_Kind", 
     30 : "Two_Pair",
     20 : "One_Pair",
     10 : "High_Card"
}
def winner(player1_check, check): 
    player = 0
    win = player1_check[-1]
    for i in range(len(check)): 
        if check[i][-1] > win: 
            win = check[i][-1]
            player = i+1
        elif check[i][-1] == win: 
            player = "mult"
    if win in winning_hands: 
        hand = winning_hands[win]
    return hand, win, player 
'''
CARD COUNTER
'''
# Hi-Lo Counter
def player_card_count(running_count, new_cards): 
    values = [n.numval for n in new_cards]
    for i in range(len(values)): 
        if 2 <= values[i] <= 6: 
            running_count += 1
        elif 7 <= values[i] <= 9:
            running_count += 0 
        else: 
            running_count -= 1 
    return running_count
def opponent_card_count(hands):
    values = []
    running_count = 0
    for i in range(len(hands)): 
        values.extend([n.numval for n in hands[i]])
    for i in range(len(values)): 
        if 2 <= values[i] <= 6: 
            running_count += 1
        elif 7 <= values[i] <= 9:
            running_count += 0 
        else: 
            running_count -= 1 
    return running_count
def community_card_count(community_cards):
    running_count = 0 
    values = [n.numval for n in community_cards]
    for i in range(len(values)): 
        if 2 <= values[i] <= 6: 
            running_count += 1
        elif 7 <= values[i] <= 9:
            running_count += 0 
        else: 
            running_count -= 1 
    return running_count
def total_card_count(player_hand, hands, community):
    running_count = 0  
    values = [n.numval for n in player_hand]
    for i in range(len(hands)): 
        values.extend([n.numval for n in hands[i]])
    values.extend([n.numval for n in community])
    for i in range(len(values)): 
        if 2 <= values[i] <= 6: 
            running_count += 1
        elif 7 <= values[i] <= 9:
            running_count += 0 
        else: 
            running_count -= 1 
    return running_count
