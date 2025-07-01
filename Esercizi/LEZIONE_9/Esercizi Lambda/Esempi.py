# moltiplicazione int
from typing import Callable 

multiply: Callable[[int, int], int] = lambda a, b: a * b 
print(multiply(3, 10))

# quadrato del numero
from typing import Callable 

square: Callable[[int], int] = lambda x: x ** 2 
print(square(5))

# moltiplicazione float 
from typing import Callable

multiply: Callable[[float, float], float] = lambda a, b: a * b 
print(multiply(3, 4))

def multiply(a:float, b:float) -> float:
    return a * b

# condizione if/else
from typing import Callable

positive_or_negative: Callable[[int], int] = lambda x: "Positivo" if x > 0 else "Zero o Negativo"
print(positive_or_negative(5))
print(positive_or_negative(-3))

def positive_or_negative(x:int) -> str:
    if x > 0:
        return "Positivo"
    else:
        return "Zero o Negativo"
    

# filter()
from typing import Callable

nums:list[int] = [1, 2, 3, 4, 5]
evens:list[int] = list(filter(lambda x: x % 2 == 0, nums))
odds:list[int] = list(filter(lambda x: x % 2 != 0, nums))
print(evens)
print(odds)
    

# sorted()
from typing import Callable 

names:list[str] = ["Alice", "Bob", "Charlie"]
sorted_by_lenght = sorted(names, key=lambda name: len(name))
print(sorted_by_lenght)


# regex + lambda 
import re 
from typing import Callable 

words:list[str] = ["abc123", "456", "43", "hello", "98abc", "test999"]

only_digit:list[str] = list(filter(lambda x: re.fullmatch(r'\d+', x), words))
only_words:list[str] = list(filter(lambda x: re.fullmatch(r'[a-zA-Z]+', x), words))
print(only_digit)
print(only_words)


# regex + lambda 
text:str = "Price: 100 dollars, Tax: 20 dollars"
new_text:str = re.sub(r'\d+', lambda x: str(int(x.group()*2)), text)
print(new_text)

