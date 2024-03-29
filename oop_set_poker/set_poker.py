# Using Set


import random 
from operator import itemgetter 


suits = ['S','H','C','D']
cardranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 
        'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}


def deck(shuffled=False): 
    d = [''.join((rank,suit)) for suit in suits for rank in cardranks]
    if shuffled:
        random.shuffle(d)
    return d 

class POKERHAND: 

    # cls variables attached to the class itself, shared among every instance 
    @classmethod 
    def from_string(cls, hand, sep=' '): 
        #cards = [(x[0],x[1]) for x in hand]
        cards = [(x[0], x[1]) for x in hand.split(sep)]
        ranks = [cardranks[x[0]] for x in cards]
        suits = [x[1] for x in cards]

        poker_hand = cls()
        poker_hand._cards = cards
        poker_hand._ranks = ranks 
        poker_hand._suits = suits 

        return poker_hand
    def __init__(self): 
        self._cards = None
        self._ranks = None
        self._suits = None 
        self._ordered = []


    @property 
    def cards(self): 
        return self._cards 
    @property
    def ranks(self): 
        return self._ranks
    @property
    def suits(self): 
        return self._suits
    @property 
    def ordered(self): 
        if self._ordered: 
            return self._ordered
        rank_counts = list(set([(i, self._ranks.count(i)) for i in self._ranks]))
        return sorted(rank_counts, key=itemgetter(1,0), reverse=True)
    @property
    def score(self): 
        # bitwise operators - bitwise left shift -> multiplying by power of 2 
        score = 1 << 0 
        if self.pair(): score <<= 1
        return score 

    def __lt__(self,other): 
        if self.score < other.score: return True
        if self.score > other.score: return False 

        for a, b in zip(self.ordered, other.ordered): 
            if a[0] < b[0]: return True 
            if a[0] > b[0]: return False 
        return False 
    # more informational string than the __str__() which returns more human readable 
    def __repr__(self): 
        return " ".join(["".join([str(x[0]), str(x[1])]) for x in self._cards]) + "Score: {}".format(self.score)
    
class SINGLEPOKERHAND(POKERHAND): 
    def pair(self): 
        return len(set(self._ranks)) == 1 
class BESTPOKERHANDS(POKERHAND): 
    def flush(self): 
        return len(set(self._suits)) == 1 
    def straight(self): 
        return len(set(self._ranks)) == 5 and max(self._ranks) - min(self._ranks) == 4 or \
            (len(set(self._ranks)) == 5 and \
            max(self._ranks) == 14 and \
            sum(self._ranks) == 28)
    def straight_flush(self): 
        return self.flush() and self.straight()
    def four_of_a_kind(self): 
        return len(set(self._ranks)) == 2 and self.ordered[0][1] == 4 
    def full_house(self): 
        return len(set(self._ranks)) == 2 and self.ordered[0][1] == 3 and \
        self.ordered[1][1] == 2 
    def three_of_a_kind(self): 
        return len(set(self._ranks)) == 3 and self.ordered[0][1] == 3 
    def two_pairs(self): 
        return len(set(self._ranks)) == 3 and self.ordered[0][1] == 2 
    def pair(self): 
        return len(set(self._ranks)) == 4 
    
    @property
    def score(self): 
        score = 1 << 0
        if self.four_of_a_kind(): score <<= 7 
        if self.full_house(): score <<= 6
        if self.flush(): score <<= 5 
        if self.straight(): score <<= 4 
        if self.three_of_a_kind(): score <<= 3
        if self.two_pairs(): score <<= 2 
        if self.pair(): score <<= 1 

        return score 
    
'''
RUNNING THE ABOVE CODE
'''
if __name__ == '__main__': 
    #block1
    hand = 'AC 2S 3C 4H 5S'
    assert BESTPOKERHANDS.from_string(hand).straight() == True 
    hand = 'AC 2S 3C 4H 5S' 
    print(BESTPOKERHANDS.from_string(hand).ordered)

    #block2
    hand = '8C TS JC 9H 7S'
    print("Hand {}: Is Straight?".format(hand), BESTPOKERHANDS.from_string(hand).straight())
    print("Hand {}: ordered".format(hand), BESTPOKERHANDS.from_string(hand).ordered)
    
    #block3
    hand = '8C 8S 8D 8H 7S'
    print(BESTPOKERHANDS.from_string(hand).ordered)
    print("Hand {}: Four of a Kind".format(hand), BESTPOKERHANDS.from_string(hand).four_of_a_kind())

    #block4
    hand = '8C 8S'
    mph = SINGLEPOKERHAND.from_string(hand)
    print(mph.score)

    #block5
    x = '9S:JC 6C:9D 2S:3D 6H:4S QC:7H TD:8D JS:7C 8H:4D 9C:4H:9H:JH:8S 4 0 1 0'
    from itertools import combinations
    h1 = '9S:JC'
    h2 = '6C:9D'
    for c in combinations('9C:4H:9H:JH'.split(':'), 3): 
        h11 = ":".join([h1, ":".join(c)])
        h21 = ":".join([h2, ":".join(c)]) 
        ph11 = BESTPOKERHANDS.from_string(h11, sep=":")
        ph21 = BESTPOKERHANDS.from_string(h21, sep=":")
        print(h11, ph11.score, h21, ph21.score, ph11 > ph21)

    #block6
    print("================")
    h1 = '2H:9S'
    h2 = '2D:2S'
    for c in combinations('4C:AC:9D:6D:6S'.split(':'), 3):
        h11 = ':'.join([h1,':'.join(c)])
        h21 = ':'.join([h2, ':'.join(c)])
        ph11 = BESTPOKERHANDS.from_string(h11, sep=':')
        ph21 = BESTPOKERHANDS.from_string(h21, sep=':')
        print(h11, ph11.score, h21, ph21.score, ph11>ph21)



