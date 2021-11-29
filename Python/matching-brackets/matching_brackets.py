def is_paired(input_string):
    brackets_match = {
        "[": "]",
        "{": "}",
        "(": ")",
    }
    brackets = []
    for bracket in input_string:
        if bracket in "[{(":
            brackets.append(tuple((bracket, brackets_match[bracket])))
            print(brackets)
        elif bracket in "]})":
            try:
                if bracket == brackets[-1][1]:
                    del brackets[-1]
                else:
                    return False
            except IndexError:
                return False

    return len(brackets) == 0
