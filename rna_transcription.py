def to_rna(dna_strand):
    result = ''
    for i in dna_strand:
        if i == 'G':
            result += 'C'
        elif i == 'C':
            result += 'G'
        elif i == 'T':
            result += 'A'
        elif i == 'A':
            result += 'U'
    return result

