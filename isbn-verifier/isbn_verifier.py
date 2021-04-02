def is_valid(isbn):
    list = [int(i) for i in isbn[::-1] if i.isdigit()]
    result = 0
    if isbn.endswith('X'):
        list.insert(0, 10)
    for x, y in enumerate(list):
        result += (x + 1) * y
    return (result % 11) == 0 and (len(list) == 10)


print(is_valid('3598215088'))
