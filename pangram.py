list = [chr(i) for i in range(97, 123)]


def is_pangram(sentence):
    return all(i in sentence.lower() for i in list)


print(is_pangram('the_quick_brown_fox_jumps_over_the_lazy_dog'))
