from math import prod


def largest_product(series, size):
    if size < 0:
        raise ValueError('Size must be greater or equal to 0')
    products = []
    result = []
    for i in range(len(series) - size + 1):
        products.append([int(num) for num in series[i: i+size]])
    result.append([prod(i) for i in products])
    return max(result[0])