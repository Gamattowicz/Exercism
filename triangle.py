def is_triangle(sides):
    return (0 not in sides) and (sides[0] + sides[1] >= sides[2] and sides[0]
                                 + sides[2] >= sides[1] and sides[1] + sides[
                                     2] >= sides[0])


def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3