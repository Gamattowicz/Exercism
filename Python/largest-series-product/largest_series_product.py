from math import prod


def largest_product(series, size):
    if size < 0 or size > len(series):
        raise ValueError('Incorrect size!')
    products = [int(i) for i in series]

    return max(prod(products[i: i+size]) for i in range(len(series) - size +
                                                        1))