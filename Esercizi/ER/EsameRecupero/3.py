def filter_and_square(nums: list[int], soglia: int) -> list[int]:
    square: list = []
    for num in nums:
        if num > soglia and num % 2 == 0:
            square.append(num**2)
    return square 


def filter_and_square1(nums: list[int], soglia: int) -> list[int]:
    squares = [num**2 for num in nums if num > soglia and num % 2 == 0]
    return squares 


def filter_and_square2(nums: list[int], soglia: int) -> list[int]:
    return [num**2 for num in nums if num > soglia and num % 2 == 0]



def filter_and_square(nums: list[int], soglia: int) -> list[int]:
    nuova_lista = []
    for num in nums:
        if num > soglia and num % 2 == 0:
            nuova_lista.append(num**2)
    return nuova_lista

def filter_and_square(nums: list[int], soglia: int) -> list[int]:
    return [num**2 for num in nums if num > soglia and num % 2 == 0]