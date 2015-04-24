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

def generate_DNA_String(ML,NM):
    DNA_String = ""
    for i in range(0,ML):
            DNA_String += random.choice(nucleotides)
    global variable
    if(ML-NM>0):
        variable = random.randint(0, ML-NM)
    else:
        variable = random.randint(NM,ML)

    return DNA_String

ML = int(input("Please enter a positive integer as the motif length\n"))
NM = int(input("Please enter a non-negative integer as the number of variable positions\n"))
SL = int(input("Please enter a positive integer as the sequence length\n"))
SC = int(input("Please enter a positive integer as the sequence count\n"))


nucleotides = ['A','G','C','T']
sequence_list = generate_sequences(SL,SC)
DNA_String = generate_DNA_String(ML,NM)
print(DNA_String)
print(variable)