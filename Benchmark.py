__author__ = 'Arpit'
def generate_sequences(SL,SC):
    for i in range(1,SC):
        print(i*SL+SC,"\n")

ML=int(input("Please enter a positive integer as the motif length\n"))
NM=int(input("Please enter a non-negative integer as the number of variable positions\n"))
SL=int(input("Please enter a positive integer as the sequence length\n"))
SC=int(input("Please enter a positive integer as the sequence count\n"))
generate_sequences(SL,SC)