def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    table = scores
    result = []
    if len(scores) >= 3:
        for i in range(3):
            result.append(max(table))
            table.remove(max(table))
    else:
        for i in range(len(scores)):
            result.append(max(table))
            table.remove(max(table))
    return result


print(personal_top_three([30, 70]))
