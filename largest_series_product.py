from math import prod


def largest_product(series, size):
    if size < 0 or size > len(series):
        raise ValueError('Size must be greater or equal to 0')
    products = []
    for i in range(len(series) - size + 1):
        products.append([int(num) for num in series[i: i+size]])
    return max([prod(i) for i in products])