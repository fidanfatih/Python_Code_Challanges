"""
https://edabit.com/challenge/vQgmyjcjMoMu9YGGW
Simplified Fractions
Create a function that returns the simplified version of a fraction.

Examples
simplify("4/6") ➞ "2/3"

simplify("10/11") ➞ "10/11"

simplify("100/400") ➞ "1/4"

simplify("8/4") ➞ "2"
Notes
A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator. For example, 4/6 is not simplified, since 4 and 6 both share 2 as a factor.
If improper fractions can be transformed into integers, do so in your code (see example #4).
"""


def simplify ( fraction ) :
    num , den = int(fraction.split('/') [ 0 ]) , int(fraction.split('/') [ 1 ])
    for i in range(min(num , den) , 0 , -1):
        if not num % i and not den % i and (den/i>1):
            return "%d/%d"% (num//i,den//i)
        elif not num % i and not den % i:
            return "%d"% (num//i)


print(simplify("70/100"))
