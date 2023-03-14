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




