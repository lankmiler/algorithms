def fibonacci_multiplication(x, y):
    Z = []
    m_list = list(sorted([int(char) for char in str(x)], reverse=True))
    n_list = list(sorted([int(char) for char in str(y)], reverse=True))

    hold = 0
    for item in range(0, len(m_list) + len(n_list)):
        for i in range(0, len(m_list)):
            for j in range(0, len(n_list)):
                if i + j == item:
                    hold = hold + m_list[j] * n_list[i]
        Z.append(int(hold % 10))
        hold = hold / 10
    acc = 0
    for i in range(0, len(Z)):
        acc = (pow(10, i) * Z[i]) + acc
    return acc

assert((15*13) == fibonacci_multiplication(15, 13))