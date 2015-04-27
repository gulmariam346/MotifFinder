__author__ = 'Arpit'
variable = -999999
import random
import math

def generate_sequences(SL,SC):
    sequence_list = []
    for i in range(0,SL):
        random_sequence = ""
        for i in range(0,SC):
            random_sequence += random.choice(nucleotides)
        sequence_list.append(random_sequence)
    return sequence_list

def generate_motif(ML,NM):
    motif = ""
    for i in range(0,ML):
            motif += random.choice(nucleotides)
    global variable
    if(ML-NM>0):
        variable = random.randint(0, ML-NM)
    else:
        variable = random.randint(NM,ML)
    return motif

def generate_binding_sites(motif,NM,ML):
    binding_sites = []

    for i in range(0,SC):
        binding_site=""
        for j in range(0,ML):
            if i in range(variable,variable+NM):
                binding_site + random.choice(nucleotides)
            else:
                binding_site + motif[i]

        binding_sites.append(binding_site)
    return binding_sites

ML = int(input("Please enter a positive integer as the motif length\n"))
NM = int(input("Please enter a non-negative integer as the number of variable positions\n"))
SL = int(input("Please enter a positive integer as the sequence length\n"))
SC = int(input("Please enter a positive integer as the sequence count\n"))


#5
'''5)	“Plant”	one sampled	site	at	a	random	location	in	each	random	sequence
generated	in	step	2.	“Planting”	a	site	means	overwriting	the	substring	at	that
location	with	the	site.'''
def planting():
    for sequence in sequence_list:
        overwrite = random.choice(sequence)
        overwrite = sampled_site

sampled_site=0
nucleotides = ['A','G','C','T']
sequence_list = generate_sequences(SL,SC)
motif = generate_motif(ML,NM)
binding_sites = generate_binding_sites(motif,NM,ML)
print(motif)
print(variable)
print(binding_sites)

