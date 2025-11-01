def filter_and_concat(nums: list[int], min_value: int) -> str:
    nuova_lista = []
    for num in nums:
        if num > min_value:
            nuova_lista.append(str(num))
    stringa = ", ".join(nuova_lista)
    return stringa

def filter_and_concat1(nums: list[int], min_value: int) -> str:
    return ", ".join([str(num) for num in nums if num > min_value])


print(filter_and_concat([1, 4, 5, 3, 6, 77, 72], 15))
print(filter_and_concat1([1, 4, 5, 3, 6, 77, 72], 15))


def filter_and_concat2(nums: list[int], min_value: int) -> str:
    nuova_lista = []
    for num in nums:
        if num > min_value:
            nuova_lista.append(str(num))
    return ", ".join(nuova_lista)

print(filter_and_concat2([1, 5, 4, 9, 82], 4))