# [set_poker_table.py](set_poker_table.py) Notes
---

- [Decorators](decorators.md)

## `class POKER_PLAYER`
---
- `__init__`
    - `self._own_cards` = private variable 
    - a leading underscore indicates internal use only 
- `@property` - enables you to modify private variables 
    - `own_cards`
        - returns players cards from private variable initialized above 
- `__repr--`
    - returns a printable string representation of object 
    - here it is printing a string of the players cards 

## `class POKER_TABLE`
--- 
- `__init__(self, players, deck)`
    - PLAYERS, DECK variables defined with class initiation: 
        - `self._total_players`, `self._deck`
    - `self._players`: add `POKER_PLAYER()` class object for each player 
    - `self._ deal/flop/turn/river _winner` = all **-1**
    - EMPTY LISTS: 
        - `self._community_cards`, `self._burnt_cards1` 
        - `self._ace_high_players`, `self._pair_players`, `self._mini_flush_players`
    - EMPTY DICTIONARY:
        - `self._table_ranks`    
- `@property -> players(self)`
    - *GETTER*
    - return private *list* variable `self._players` 
        - aka one `POKER_PLAYER()` class object for each player 
- **Poker Rounds**
    - `deal()`: deal two cards to each player in `self._players` 
        - pop card from `self._deck`
    - `burn_card()`: pop one card from `self._deck`
    - `flop()`: burn a card
        - add three cards to `self._community_cards`
    - `turn()`: burn a card 
        - add one card to `self._community_cards`
    - `river()`: burn a card 
        - add one card to `self._community_cards`
- `@property -> table_ranks(self)`
    - *GETTER*
    - return *sorted* private *dictionary* variable `self._table_ranks` 
        - `key=lambda kv: kv[0]`: returns value at index 0 
            - `self._table_ranks[0]` = winner of specified rounds in `one_game(self)
            - returns top player
- `__repr__`
    - return list of: 
        - *players, community cards*
        - *deal, flop, turn*, and *river winners* 
        - if *deal, flop*, and *turn winners* are the same as the *river winner*
        - count of *ace high players*, *pair players*, and *mini flush players
        - if *river winner is an *ace high player, a *pair player*, or a *mini flush players*
    - **in printable format**
- `rank_players(self, pre_flop=False)`
    - *cannot rank before the flop*
    - cerate a dictionary to hold `player_hands` 
    - `if pre_flop:` is True: (player only has two cards, no community cards yet)
        - for each player in `self._players` -> `player_hands[i]`
            - `SINGLEPOKERHAND.from_string(" ".join(player.own_cards))`
                - return list of player's cards with spaces inbetween values in the list 
                - assign to `player_hands[i]`
                    - use of `SINGLEPOKERHAND(POKERHAND)` from [set_poker](set_poker.py)
                        - if pair, return TRUE 
                        - here, using `from_string()` from class `POKERHAND`
                    - `.from_string()` in `POKERHAND` class
                        - ***@classmethod***: [able to access/modify class state, removing redundancy](decorators.md) 
                        - modifying variables from `POKERHAND`'s `__init__`
                    - 
                    - `" ".join(player.own_cards)`: for individual player from list of `self._players`
                        - `.own_cards` = `@property -> own_cards` 
                            - *GETTER* 
                            - returns `POKER_PLAYER` class's list `self._own_cards()`
                        - joins into one list object 
            - if *max* of `.ranks` == 14: they have ace
                - class `POKERHAND` ***@property***
                    - returns numbers values from cards 
                - add player index identification to `self._ace_high_players`
            - if `.score` == 2: they have two pairs 
                - class `POKERHAND` ***@property*** 
                    - bitwise operators -> increase by one left shift to distinguish players whose hands are pairs 
                        - pairs: (from *SINGLEPOKERHAND(POKERHAND)*)
                - add player index identification to `self._pair_players`
            - if len(set(`.suits`)) == 1: they have a mini flush 
                - class `POKERHAND` ***@property***
                    - returns suit values from cards 
                - add player index idenitification to `self._mini_flush_players`
    - `else:` pre-flop=False *(default)*
        - for each player in `self._players` -> `player_hands[i]`
            - create empty list for `possible_hands`
            - **WAY ABOVE** `from itertools import combinations`
            - sort through combinations of *three* `self._community_cards`
                - append `BESTPOKERHANDS.from_string(" ".join(hand))` to `possible_hands`
                    - `.from_string` comes from `POKERHAND` class 
                        - defines cards, ranks, and suits list objects 
                    - `hand` = combination of individual players original hands, and the combo of community cards 
                    - joins cards into single list object, separated by spaces 
            - `player_hands[i] = sorted(possible_hands, reverse=True)[0]`
                - appends best hand of the specifc player to the `player_hands` list 
    - `players = sorted(player_hands.items(), key=lambda kv:kv[1], reverse=True)`
        - sort player hands by the contents of their hands, not their player index 
            - from `key=lambda kv: kv[1]`
        - reverse the list so the highest value hand is first 
    - for each player: 
        - assign their ID to `self._table_ranks` dictionary 
            - retrievable by `table_ranks` *@property*
        

                

- `one_game()`
    - For Each Round: *Deal, Flop, Turn, River* 
        - `.rank_players()` after each round 
        - Set each individual round winner from the `self._table_ranks[0]` value 


## RUNNING CODE WITH `if __name__ == '__main__':`
- Executes Code When File Runs as a Script -> *Not When Imported As Module*
    - conditional block -> if name == main -> returns true and executes 
        - module name set to "__main__"
        - thus only code executed within the specific file will run 
    
- Block 1 
    - identify number of players and game count 
- Block 2
    - Create Tuple of results for each game: *store multiple items in a single variable*
        - Each Player and Their Starting Hands 
        - Community Cards + Each Round's Winner 
        - Number of Ace, Pair, and Flush Players and if any of such players were the winner 
- Block 3 
    - create empty list of games
    - for each game: 
        - define `POKER_TABLE` class object 
        - run the game, convert table to a string, split table string 
        - each `gameval` belongs to a column defined in Block 2
            - turn into `PokerGame` tuple 
        - append to game list 
- Block 4 
    - identify how many ace, pair, or flush hands exist, and if they are winners 
    - print out of how many games ace high at the deal wins 



