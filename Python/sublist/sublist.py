SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    list_1 = str(list_one)[1:-1]
    list_2 = str(list_two)[1:-1]
    if list_one == list_two:
        return EQUAL
    elif list_1 in list_2:
        return SUBLIST
    elif list_2 in list_1:
        return SUPERLIST
    else:
        return UNEQUAL
