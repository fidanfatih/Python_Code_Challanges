"""
https://edabit.com/challenge/hbrEwrcSAQTbP9fKS
Catalan Number
Create a function that returns the nth catalan number.In combinatorial mathematics, the Catalan numbers form a sequence of natural numbers that occur in various counting problems, often involving recursively-defined objects. They are named after the Belgian mathematician Eugène Charles Catalan (1814–1894). For more info, check out the resource tab.

Examples
get_catalan_number(0) ➞ 1

get_catalan_number(6) ➞ 132

get_catalan_number(8) ➞ 1430
Notes
Inputs are zero and positive integers.
1/(n1+1)*C(2n,n1)
(2n)!/(n1+1)!*n1!
"""
import math


def get_catalan_number(n):
    return int(math.factorial(2*n)/(math.factorial(n+1)*math.factorial(n)))
# def get_catalan_number(n1):
#     return int(1/(n1+1)*math.comb(2*n1,n1))


print(get_catalan_number(6))
