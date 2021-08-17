def primes(limit):
    list_prime = list(range(2, limit + 1))
    for i in range(2, round(limit ** 0.5) + 1):
        for j in range(1, limit):
            if i + i*j > limit:
                continue
            elif i + i*j in list_prime:
                list_prime.remove(i + i*j)
    return list_prime
