"""DNA analysis for a crime investigation"""

sample = ['GTA','GGG','CAC']

"""Take file, read it, add the file's contents to an empty string, and return the updated string."""
def read_dna(dna_file):
    dna_data = ""
    with open(dna_file, "r") as f:
        for line in f:
            dna_data += line
    return dna_data

"""take a string, create a list of codons from that string, and return the list."""
def dna_codons(dna):
    codons = []
    for i in range(0, len(dna), 3):
        if (i+3) < len(dna):
            codons.append(dna[i:i+3])
    return codons

"""iterate through both the sample and a suspect's DNA."""
def match_dna(dna):
    matches = 0
    for codon in dna:
        if codon in sample:
            matches += 1
    return matches

""" determine if a suspect is the criminal"""
def is_criminal(dna_sample):
    dna_data = read_dna(dna_sample)
    #chop the string into a list of codons
    codons = dna_codons(dna_data)
    #match the sample with the DNA
    num_matches = match_dna(codons)
    if num_matches >= 3:
        print "The number of matches is: %s. Continue investigation." % (num_matches)
    else:
        print "The number of matches is: %s. The suspect can be freed" % (num_matches)

is_criminal("pypsuspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")

