def triplets_with_sum(number):
    result = []
    for a in range(1, number//3):
        for b in range(a+1, number//2):
            if a + b + ((a**2 + b**2)**0.5) == number:
                result.append([a, b, (a**2 + b**2)**0.5])
    return result

print(triplets_with_sum(12))