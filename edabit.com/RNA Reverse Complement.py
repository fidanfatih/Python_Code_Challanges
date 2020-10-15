"""
https://edabit.com/challenge/M8jNckAgpC5ZFkhhG
Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. The RNA will be represented as a string containing only the characters "A", "C", "G" and "U". Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:

original -> complement
"AAA" -> "UUU"
"UUU" -> "AAA"
"GGG" -> "CCC"
"CCC" -> "GGG"
"GGAACC" -> "CCAAGG"
Your function should find the complement on the right AND also reverse the resulting string.

Examples
reverse_complement("GUGU") ➞ "ACAC"

reverse_complement("UCUCG") ➞ "CGAGA"

reverse_complement("CAGGUAGC") ➞ "ACCUG"
Notes
You can assume all input seqeuences will be valid.
"""
# def reverse_complement(dna):
#     rna={"A":"U","U":"A","G":"C","C":"G"}
#     return ''.join([rna[i] for i in dna][::-1])

# def reverse_complement(input_sequence):
# 	return input_sequence.translate(str.maketrans('AXGC', 'XACG'))[::-1]

def reverse_complement(input_sequence):
	return ''.join(['G'*(i=='C') or 'C'*(i=='G') or 'A'*(i=='U') or 'U'*(i=='A')  for i in input_sequence][::-1])

print(reverse_complement("CAGGUAGC"))

