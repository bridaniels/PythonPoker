# **Simulating Poker Games with Python: Using `Set` and Decorators**
---
- [GitHub Repo Referenced](https://github.com/gabhijit/pycon/tree/master/2019/poker)


## [Decorators Explained](decorators.md)    



## Define Deck and Hands [.py](set_poker.py)
---
- Define Deck as List: `['S3', 'H4', 'H8', 'SQ', ...]`

### `class POKERHAND`
- `from_string()`
    - make lists of cards, ranks, and suits
    - `poker_hand` = `@classmethod` (cls) -> removes redundancy  
- `cards()`, `ranks()`, `suits()`, `ordered()`, and `score()`
    - `@property` Decorator Elements 
    - Returns property attributes of a class
- `__lt__` Less Than Magic Operator 
    - Highest Score or Highest Card in Ordered 
        - depends on what is put into (*other*)
    - if score ***x*** lower than score ***y*** = True, else False 
    - then pick who has the highest card
    - False if neither score or ordered 
- `__repr__` Printable Representation of Object as a String 
    - Returns Readable String when `print()` is called 

### `class SINGLEPOKERHAND(POKERHAND)`

### `class BESTPOKERHANDS(POKERHAND)`
- Define What Possible Hand's Exist 
    - **Flush**: 5 cards of same suit 
        - length of `set(self._suits) == 1` -> only one suit 
    - **Straight**: 5 numbers in order 
        - lenght of `set(self._ranks) == 5` -> need 5 different ranks 
        - max rank - min rank == 4 -> should be in order 
        - **OR** if `set(self._ranks) == 5` and max rank == 14 (ACE) and the sum of ranks == 28 
            - 14 + 2 + 3 + 4 + 5 = 28 
            - Ace can be a high or low card in a straight 
    - **Straight Flush**: 5 numbers in order of the same suit 
        - call straight and flush functions (recursive) 




