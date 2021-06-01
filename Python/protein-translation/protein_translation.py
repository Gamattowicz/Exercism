def proteins(strand):
    amino_acids = {
        'AUG': 'Methionine',
        ('UUU', 'UUC'): 'Phenylalanine',
        ('UUA', 'UUG'): 'Leucine',
        ('UCU', 'UCC', 'UCA', 'UCG'): 'Serine',
        ('UAU', 'UAC'): 'Tyrosine',
        ('UGU', 'UGC'): 'Cysteine',
        'UGG': 'Tryptophan',
        ('UAA', 'UAG', 'UGA'): 'STOP',
        }
    codons = [strand[i: i + 3] for i in range(0, len(strand), 3)]
    result = []
    for codon in codons:
        for key in amino_acids.keys():
            if codon in key:
                if amino_acids[key] == 'STOP':
                    return result
                result.append(amino_acids[key])
    return result