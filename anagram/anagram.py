def find_anagrams(word, candidates):
    return [i for i in candidates if sorted(i.lower()) == sorted(word.lower())
            and word.lower() != i.lower()]


print(find_anagrams('master', ["stream", "pigeon", "maters"]))
