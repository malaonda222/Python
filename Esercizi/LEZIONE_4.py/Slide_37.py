# kwargs
# def total_price(*args):
#     total:float = sum(args)
#     return total
# print(total_price(2.99, 4.55, 8.90))


def total_price(**kwargs):
    total:float = 0
    for product, price in kwargs.items():
        print(f"{product}: {price} euro")
        total+=price
    return round(total, 2)
print(total_price(coffee=2.99, juice=8.00, water=3.00))
