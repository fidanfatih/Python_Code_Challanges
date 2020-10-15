# https://edabit.com/challenge/j9zed4GnykS48W6vh
import math
def digits(num):
    d=int(math.log10(num)+1)
    return d*num-int("1"*d)

print(digits(58473029386609125789))
