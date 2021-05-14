def transform(legacy_data):
    lib = {}
    for i, v in legacy_data.items():
        for letter in v:
            lib[letter.lower()] = i
    return lib

