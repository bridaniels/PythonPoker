# Set Poker Table 

from set_poker import BESTPOKERHANDS, SINGLEPOKERHAND
from set_poker import deck 
from itertools import combinations
from collections import namedtuple


class POKER_PLAYER: 
    def __init__(self): 
        self._own_cards = []
    
    @property
    def own_cards(self): 
        return self._own_cards
    
    def __repr__(self):
        return ":".join(self._own_cards)
    

class POKER_TABLE: 

    def __init__(self, players, deck): 
        self._total_players = players
        self._players = [POKER_PLAYER() for i in range(players)]
        self._community_cards = []
        self._deck = deck 
        self._burnt_cards = []
        self._table_ranks = {}

        self._deal_winner = - 1
        self._flop_winner = -1
        self._turn_winner = -1 
        self._river_winner = -1 

        self._ace_high_players = []
        self._pair_players = []
        self._mini_flush_players = []

    @property
    def players(self): 
        return self._players 
    

#https://github.com/gabhijit/pycon/blob/master/2019/poker/pokertable.py