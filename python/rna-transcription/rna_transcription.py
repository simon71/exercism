def to_rna(dna_strand):
    transcribed_dna = {
            'G':'C',
            'C':'G',
            'T':'A',
            'A':'U'
            }
    rna = ""
    for nuc in dna_strand:
        rna = rna + transcribed_dna[nuc]
    return rna
