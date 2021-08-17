secrets = {
    1: 'wink',
    2: 'double blink',
    3: 'close your eyes',
    4: 'jump'
}


def commands(number):
    num = bin(number)[2:][::-1]
    results = [secrets[i] for i, v in enumerate(list(num)[:4], 1) if v == '1']
    return results[::-1] if number >= 16 else results