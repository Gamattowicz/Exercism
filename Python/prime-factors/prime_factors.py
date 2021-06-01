def factors(value):
    prime_list = []
    factor = 2
    while value != 1:
        if (value / factor).is_integer():
            prime_list.append(factor)
            value = value / factor
        else:
            factor += 1
    return prime_list

