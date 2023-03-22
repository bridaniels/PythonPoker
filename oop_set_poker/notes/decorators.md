# [Decorators](https://www.geeksforgeeks.org/decorators-in-python/)
---
- Functions are *first class objects* 
    - can be used or passed as arguments 
    - instance of *object* type 
    - stored in variables
- Decorators are *function/class modifiers*
    - functions taken as the argument 
        - into another function 
            - then called inside wrapper 
    - Function taking a function as its only parameter and returns a function 
    - Adds new functionality to an existing function without modifying the original 
    - Helpful to "wrap" functionality with same code over and over 
    - Remove Redundancy 
    - **Metaprogramming**
        - at compile time a section of the prgram alters another section of the program 

    ```
    def DECORATOR(FUNC): 
        def round1(): 
            print("Before FUNC Execution")
            
            FUNC()
            print("After FUNC Execution")
        return round1
    
    def USED_FUNC(): 
        print("INSIDE FUNC !!")

    USED_FUNC = DECORATOR(USED_FUNC)
    USED_FUNC()

    # OUTPUT
    Before FUNC Execution 
    INISDE FUNC !!
    After FUNC Execution     
    ```
    ### Function Returns Something/Argument Passed To Function 
    ```
    def DECORATOR(FUNC):
        def round1(*args, **kwargs): 
            print("Before Execution")

            returned_val = FUNC(*args, **kwargs)
            print("After Execution")
            return returned_val 
        return round1 
    
    @DECORATOR
    def sum_two_nums(a,b):
        print("Inside the Function !!")
        return a + b
    
    a, b = 1, 2
    print("Sum = ", sum_two_nums(a,b))

    # OUTPUT 
    Before Execution 
    Inside the Function !!
    After Execution 
    Sum = 3
    ```
    - `*args` and `**kwargs` mean a tuple of positional arguments or a dictionary of keyword arguments can be passed of any length 
    

# Decorators Used in [set_poker.py](set_poker.py)
---
## [`@classmethod`](https://www.geeksforgeeks.org/classmethod-in-python/) - *built-in*
- attatched to class itself vs. an object 
- shared amongst every instance of the class
- able to access/modify the class state 
- `poker_hand` = Class Method -> removing redundancy 

## [`@property`]((https://www.geeksforgeeks.org/python-property-decorator-property/)) - *built-in*
- returns property attributes of a class 
- `cards()`, `ranks()`, `suits()`, `ordered()`, and `score()`
- built-in decorator for `property()` function 
    - functionality for getters, setters, or deleters
        - don't need to use all three
    - does not affect syntax used to access or modify attribute when public
    > - `self.variable` = unprotected 
    > - `self._variable` = protected (leading underscore) 
    >   - should not be accessed or modified outside of the class 
    >   - should only be accessed through intermediaries (getters/setters)
- **Getter**
    ```
    @property
    def suits(self): 
        return self._suits


    >>> player1_hand = POKERHAND(['2H', '9H'])  # Create Instance 
    >>> player1_hand.suits                      # Access Value
    [2,9]
    ```
- **Setter**
    ```
    @suits.setter
    def suits(self, new_suit):
        if new_suit > 0: 
            self._suit = new_suit 
        else: 
            print("Please Enter Valid New Suit")
    

    >>> player1_hand = POKERHAND(['2H', '9H'])  # Create Instance
    >>> player1_hand.suits = [4,6]              # Update Value
    >>> player1_hand.suits                      # Access Value 
    [4,6]
    ```
    - name of property included before `.setter` 
    - property name used as setter function name 
        - second parameter passed as new property *if valid* 
    - working as an intermediary -> "behind the scenes"
- **Deleter**
    ```
    @suits.deleter
    def suits(self): 
        del self._suits

    >>> player1_hand = POKERHAND(['2H', '9H'])  # Create Instance
    >>> player1_hand.suits                      # Access Value
    [2,9]
    >>> del player1_hand.suits                  # Delete Instance  
    >>> player1_hand.suits                      # Access Value
    AttributeError: 'POKERHAND' object has no attribute '_suits' 
    ```
    - name of property included before `.deleter`
    - property name used as deleter function name 
        - no second parameter 




# Magical Operator
---
- define operators in python 
- double underscores represent magic methods 
## [`__lt__(self,other)`](https://www.pythonpool.com/python-__lt__/)
- **Less Than Operator (<)**
- useful for sorting and operator overloading and comparing 
- *cannot be used directly* 
- Returns True if *less than*, Returns False if not

```
class Weight: 
    def __init__(self, weight): 
        self.weight = weight
    def __lt__(self,other):
        return self.weight < other.weight
    def __gt__(self,other): 
        return self.weight > other.weight
a = Weight(50)
b = Weight(60)
c = Weight(70)
print(a<b and b>c)

>>> False 
```

| Magic Operator |     | Symbol |
|----------------|-----|--------|
|`__lt__` | Less Than | < |
|`__gt__` | Greater Than| > |
|`__le__` | Less Than/Equal To | <= |
|`__ge__` | Greater Than/Equal To | >= |
|`__eq__` | Equal To | == |
|`__ne__` | Not Equal | != |


## [`__repr__(self)`](https://www.geeksforgeeks.org/python-__repr__-magic-method/)
- Returns printable string representation of an object 
- *gives representation of the object*
- when `print()` is called 



# References
---
- [G4G: Function Decorators](https://www.geeksforgeeks.org/function-decorators-in-python-set-1-introduction/)
- [G4G: Property Decorator](https://www.geeksforgeeks.org/python-property-decorator-property/)
- [FCC: Property Decorator](https://www.freecodecamp.org/news/python-property-decorator/)