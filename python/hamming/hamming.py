def distance(strand_a, strand_b):
    if (len(str(strand_a)) > 0 and len(str(strand_b)) > 0) and (len(strand_a) == len(strand_b)) :
        hamming_value = sum(1 for a, b in zip(strand_a, strand_b) if a != b)
        return hamming_value
    elif (len(str(strand_a)) == 0 and len(str(strand_b)) == 0):
        return 0
    else:
        raise ValueError("Strands must be of equal length.")
