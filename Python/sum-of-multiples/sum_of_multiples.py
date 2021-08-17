def sum_of_multiples(limit, multiples):
    multiples_list = []

    for i in range(limit):
        for j in multiples:
            if j != 0 and i % j == 0:
                multiples_list.append(i)
    return sum(set(multiples_list))
