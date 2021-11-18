def answer(question):
    if not (question.startswith("What is") and question.endswith("?")):
        raise ValueError("Invalid question")
    words = (
        question.replace("raised to the", "^")
        .replace("divided by", "/")
        .replace("multiplied by", "*")
        .replace("minus", "-")
        .replace("plus", "+")
        .rstrip("?")
        .split()
    )
    if len(words) < 3:
        raise ValueError("Invalid question")
    result = None
    operator = None
    for word in words[2:]:
        word_index = words.index(word)
        if (
            result is None
            and operator is None
            and (word.isdigit() or (word[1:].isdigit() and word[0] == "-"))
        ):
            result = int(word)
        elif (
            result is not None
            and operator is not None
            and (word.isdigit() or (word[1:].isdigit() and word[0] == "-"))
        ):
            if operator == "+":
                result += int(word)
            elif operator == "-":
                result -= int(word)
            elif operator == "*":
                result *= int(word)
            elif operator == "/":
                result //= int(word)
            elif operator == "^":
                result **= int(word)
            operator = None
        elif result is not None and operator is None and word in list("+-*/^"):
            operator = word
        else:
            raise ValueError("Invalid question")
    if operator == words[-1]:
        raise ValueError("Invalid question")
    return result
