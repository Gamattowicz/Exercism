def is_armstrong_number(number):
    n = str(number)
    result = 0
    for i in range(len(n)):
        result += pow(int(n[i]), len(n))
    return result == number


print(is_armstrong_number(9))
