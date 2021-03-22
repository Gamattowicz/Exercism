def square(number):
    if number < 1 or number > 64:
        raise ValueError('Number must be between 1 and 64')
    elif number == 1:
        return 1
    elif number == 2:
        return 1 * 2
    return square(number - 1) * 2


def total():
    return sum([square(i) for i in range(1, 65)])
