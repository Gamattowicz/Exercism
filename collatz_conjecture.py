def steps(number):
    steps = 0
    if number > 0:
        while number != 1:
            if number % 2 == 0:
                number = number / 2
                steps += 1
            else:
                number = number * 3 + 1
                steps += 1
        return steps
    else:
        raise ValueError('Number must be greater than 0')


print(steps(16))