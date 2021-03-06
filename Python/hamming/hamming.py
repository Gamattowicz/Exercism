def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        return sum([a != b for a, b in zip(strand_a, strand_b)])
    raise ValueError('strands are not equal')


print(distance("GGACTGAAATCTG", "GGACTGAAATCTG"))
