def classify(number):
    if number <= 0:
        raise ValueError('Enter positive number')

    factors = sum([factor for factor in range(1, number) if number % factor == 0])
    if factors == number:
        return 'perfect'
    elif factors > number:
        return 'abundant'
    else:
        return 'deficient'
