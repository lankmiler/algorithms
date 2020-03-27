def peasant_multiplication_recursive(x, y, prod=0):
    if x > 0:
        if x%2 != 0:
            prod = prod + y
        prod = peasant_multiplication_recursive(int(x/2), int(y + y), prod)
    return prod
assert((123*456) == peasant_multiplication_recursive(123, 456))
