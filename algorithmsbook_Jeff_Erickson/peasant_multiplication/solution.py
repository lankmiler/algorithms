def peasant_multiplication(x, y):
    prod = 0
    while x > 0:
        if x%2 != 0:
            prod = prod + y
        x = int(x / 2)
        y = int(y + y)
    return prod

assert((123*456) == peasant_multiplication(123, 456))
