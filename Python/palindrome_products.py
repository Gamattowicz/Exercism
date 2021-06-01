def palindromes(start, end):
    products = []
    factors = []
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            if str(i * j) == str(i * j)[::-1]:
                if [j, i] in products:
                    continue
                products.append([i, j])
                factors.append(i * j)
    return products, factors


def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError('Max factors must be greater than min factor')
    elif min_factor == max_factor or min_factor == max_factor - 1:
        return None, []
    factors, value = palindromes(min_factor, max_factor)
    indexes = [i for i, v in enumerate(value) if v == max(value)]
    factors2 = [factors[i] for i in indexes]

    return max(value), factors2


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError('Max factors must be greater than min factor')
    elif min_factor == max_factor or min_factor == max_factor - 1:
        return None, []
    factors, value = palindromes(min_factor, max_factor)
    indexes = [i for i, v in enumerate(value) if v == min(value)]
    factors2 = [factors[i] for i in indexes]

    return min(value), factors2