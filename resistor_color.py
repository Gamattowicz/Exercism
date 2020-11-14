band = ['black', 'brown', 'red', 'orange',
        'yellow', 'green', 'blue', 'violet',
        'grey', 'white']


def color_code(color):
    return band.index(color)


def colors():
    return band


print(color_code('white'))
