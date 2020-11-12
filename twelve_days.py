days = [
    ['first', 'a Partridge in a Pear Tree.'],
    ['second', 'two Turtle Doves, and '],
    ['third', 'three French Hens, '],
    ['fourth', 'four Calling Birds, '],
    ['fifth', 'five Gold Rings, '],
    ['sixth', 'six Geese-a-Laying, '],
    ['seventh', 'seven Swans-a-Swimming, '],
    ['eighth', 'eight Maids-a-Milking, '],
    ['ninth', 'nine Ladies Dancing, '],
    ['tenth', 'ten Lords-a-Leaping, '],
    ['eleventh', 'eleven Pipers Piping, '],
    ['twelfth', 'twelve Drummers Drumming, ']
]


def verse(n):
    num = days[n][0]
    present = "".join(i[1] for i in days[n:: -1])
    return 'On the {} day of Christmas my true love gave to me: {}'.format(num, present)


def recite(start_verse, end_verse):
    return [verse(n) for n in range(start_verse - 1, end_verse)]


print(recite(11, 11))
