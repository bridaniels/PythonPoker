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
- `@property` Decorator Elements 
    - Returns property attributes of a class
    - `cards()`, `ranks()`, and `suits()`
        - all returning what they are
    - `ordered(self)`
        - If `self._ordered` exists -> Easy Value Return 
        - Else: Count how many of each card rank 
            - List of sets `list(set(Rank, Count))`
            - Return: sorted list of card ranks -> `key=itemgetter(1,0)`
                - `key` transforms elements before sorting 
                - `itemgetter(1,0)` allows you to sort a table (multiple indices) 
                    - lambda also works 
                    - sorting by count, then rank (backwards from list of sets)
                - `reverse=True` -> sorting from High to Low 
    - `score(self)`
        - score defaults as `1 << 0`
            - Bitwise Operator - performs bitwise calculations - first converts integers into binary 
            - `<<` = Bitwise Left Shift: Left moved over by number of bits specified by the right 
                - shifting is equivalent to multipylying the number with power of 2 
                - `score = 1`
        - check players two dealt cards for a pair 
            - CALLS `SINGLEPOKERHAND(POKERHAND)` CLASS 
            - if there is a pair -> more bitwise left shifting 
                - `score <<= 1` == `score = score << 1`
                - `score = 2`


- `__lt__` Less Than Magic Operator 
    - Highest Score or Highest Card in Ordered 
        - depends on what is put into (*other*)
    - if score ***x*** lower than score ***y*** = True, else False 
    - then pick who has the highest card
    - False if neither score or ordered 
- `__repr__` Printable Representation of Object as a String 
    - Returns Readable String when `print()` is called 

### `class SINGLEPOKERHAND(POKERHAND)`
- Do the first two cards dealt to the player make a pair? 
    - **Pair**: 
        - with two cards dealt, should only contain one pair 

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
    - **Four of a Kind**: 4 of the same card rank -> suit does not matter 
        - in a playable hand of 5 cards, only 2 ranks will exist 
        - ordered card count of first set in the list should == 4 
    - **Three of a Kind**: 3 of the same card rank -> suit does not matter 
        - in a playable hand of 5 cards, only 3 ranks will exist 
        - ordered card count of first set in the list should == 3
    - **Full House**: 3 of a kind and a pair 
        - in a playable hand of 5 cards, only 2 ranks should exist 
        - ordered card count of first set in the list == 3
        - ordered card count of second set in the list == 2
    - **Two Pair**: Two Pairs and one High Card
        - in a playable hand of 5 cards, only 3 ranks 
        - ordered card count of the first set in the list == 2
        - No need to go any further -> Math is Mathing 
    - **Pair**: One Pair in Full Hand 
        - total of 4 different ranks in a hand of 5 cards 

- **@property** Decorator (*getter* functionality without altering main block of code - defines *score* property)
- **score(self)**: 
    - `score = 1 << 0` Bitwise Operator
        - Bitwise Left Shift -> Multiply First Number by `2**X`
        - `score = 1`
    - `score <<= 7` -> `score = score << 7`
        - `score * (2**7)`
    - returns score of the hand 
    - No need to modify code to add getter and setter functionality 
    - Score now an attribute of a poker hand 

### RUNNING CODE WITH `if __name__ == '__main__'`:
- allows you to execute code when file runs as a script, but not when imported as module 
- Conditional Block: if name == main -> returns true and executes the code
- Python sets name of a module to "__main__"
    - thus if the code is executing in the specific file (not somewhere else) the code will run 
    - if the code is imported, it will not run as it is no longer "__main__" 
- Block 1
    - `assert` -> keyword used to debug code
        - checks if condition is true or false (AssertionError)
    - checking that functions are reading/returning the code as intended 
- Block 2 
    - checking boolean + printing 
- Block 3
    - printing ordered = (rank, count) 
    - checking for functionality 
- Block 4 
    - return `SINGLEPOKERHAND` score
    - `mph.score` a property of `mph` due to `@property` decorator 
- Block 5
    - hand1 = first two cards from *x*
    - hand2 = second two cards from *x*
    - combinations -> iterates through community cards to determine which hand provides the highest value to the player 
    - prints all results from hand combinations 
- Block 6
    - ^ same as above, different hands 




# References 
--- 
- [G4G: Bitwise Operators](https://www.geeksforgeeks.org/python-bitwise-operators/)
- [RealPython: if-name-main](https://realpython.com/if-name-main-python/)
