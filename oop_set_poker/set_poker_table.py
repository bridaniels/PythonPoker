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
    #DEAL TWO CARDS TO PLAYERS 
    def deal(self): 
        for i in range(2): 
            for player in self._players: 
                player._own_cards.append(self._deck.pop())
    #BURN TOP CARD 
    def burn_card(self): 
        self._burnt_cards.append(self._deck.pop())
    #FIRST ROUND
    def flop(self): 
        self.burn_card()
        for i in range(3):
            self._community_cards.append(self._deck.pop())
    #SECOND ROUND
    def turn(self): 
        self.burn_card()
        self._community_cards.append(self._deck.pop())
    #THIRD AND FINAL ROUND
    def river(self):
        self.burn_card()
        self._community_cards.append(self._deck.pop())


    @property
    def table_ranks(self): 
        return dict(sorted(self._table_ranks.items(),
                           key=lambda kv: kv[0]))
    def __repr__(self):
        players = " ".join([str(player) for player in self._players])
        community_cards = ":".join(self._community_cards)

        return " ".join([players, community_cards, 
                         str(self._deal_winner),
                         str(self._flop_winner), 
                         str(self._turn_winner),
                         str(self._river_winner),
                         str(int(self._deal_winner == self._river_winner)), 
                         str(int(self._flop_winner == self._river_winner)), 
                         str(int(self._turn_winner == self._river_winner)), 
                         str(len(self._ace_high_players)), 
                         str(int(self._river_winner in self._ace_high_players)), 
                         str(len(self._pair_players)), 
                         str(int(self._river_winner in self._pair_players)),
                         str(len(self._mini_flush_players)),
                         str(int(self._river_winner in self._mini_flush_players))
                         ])
    
    def rank_players(self, pre_flop=False): 
        player_hands = {}
        #ANALYZE AFTER DEAL - BEFORE FIRST ROUND 
        if pre_flop: 
            for i, player in enumerate(self._players): 
                player_hands[i] = SINGLEPOKERHAND.from_string(" ".join(player.own_cards))
                if max(player_hands[i].ranks) == 14: #DO THEY HAVE ACE?
                    self._ace_high_players.append(i)
                if player_hands[i].score == 2: #TWO PAIRS 
                    self._pair_players.append(i)
                if len(set(player_hands[i].suits)) == 1: #MINI FLUSH
                    self._mini_flush_players.append(i)
        else: 
            for i, player in enumerate(self._players): 
                possible_hands = []
                for c in combinations(self._community_cards, 3): 
                    hand = player.own_cards + list(c)
                    possible_hands.append(BESTPOKERHANDS.from_string(" ".join(hand)))
                player_hands[i] = sorted(possible_hands, reverse=True)[0]
        players = sorted(player_hands.items(), key=lambda kv:kv[1], reverse=True)
        for i in range(len(players)): 
            player_id = players[i][0]
            self._table_ranks[i] = player_id



    
    def one_game(self): 
        #PRE-FLOP
        self.deal()
        self.rank_players(pre_flop=True)
        self._deal_winner = self._table_ranks[0]

        #FLOP
        self.burn_card()
        self.flop()
        self.rank_players()
        self._flop_winner = self._table_ranks[0]

        #TURN
        self.burn_card()
        self.turn()
        self.rank_players()
        self._turn_winner = self._table_ranks[0]

        #RIVER
        self.burn_card()
        self.river()
        self.rank_players()
        self._river_winner = self._table_ranks[0]

        #WINNER
        self._pot_winner = self._river_winner


'''
RUNNING ABOVE CODE 
'''

if __name__ == '__main__': 
    #Block1
    num_players = 5
    count = 5000

    #Block2
    columns = ['player'+str(i) for i in range(num_players)]
    columns += ['community_cards', 'deal_winner', 'flop_winner', 'turn_winner', 'river_winner']
    columns += ['deal_winner_is_winner', 'flop_winner_is_winner', 'turn_winner_is_winner']
    columns += ['num_ace_players', 'ace_player_is_winner']
    columns += ['num_pair_players', 'pair_player_is_winner']
    columns += ['num_mini_flush_players', 'mini_flush_player_is_winner']
    PokerGame = namedtuple('PokerGame', columns)

    #Block3
    games = []
    for i in range(count): 
        table = POKER_TABLE(num_players, deck(shuffled=True))
        table.one_game()
        gamestr = str(table)
        gamevals = gamestr.split()
        game = PokerGame(*gamevals)
        print(game)
        games.append(game)
    

    #Block4
    #ACE WINNERS
    ace_winners = sum([int(x.ace_player_is_winner) for x in games])
    ace_high_exists = sum([int(int(x.num_ace_players) > 0 ) for x in games])
    print(ace_winners, ace_high_exists)
    #PAIR WINNERS
    pair_winners = sum([int(x.pair_player_is_winner) for x in games])
    pair_player_exists = sum([int(int(x.num_pair_players) > 0) for x in games])
    print(pair_winners, pair_player_exists)
    #FLUSH WINNERS
    mini_flush_winners = sum([int(x.mini_flush_player_is_winner) for x in games])
    mini_flush_exists = sum([int(int(x.num_mini_flush_players) > 0 ) for x in games])
    mini_flush_flop_winners = sum([int(int(x.num_mini_flush_players) > 0 and x.flop_winner_is_winner) for x in games])
    print(mini_flush_winners, mini_flush_flop_winners, mini_flush_exists)

    print("%d of %d Games Where Ace High During Deal is a Winner" % (ace_winners, count))


    
#Reference
#https://github.com/gabhijit/pycon/blob/master/2019/poker/pokertable.py