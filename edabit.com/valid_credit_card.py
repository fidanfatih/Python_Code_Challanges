# https://edabit.com/challenge/XKEDTh2NMtTLSyCc2
def valid_credit_card(n):
    n1=[ int( i ) for i in str( n) ][::-1]
    for i in range ( 1, len( n1 ), 2 ): n1[i ]= n1[i ] * 2
    n1=[ n1[i ] % 10 + n1[i ] // 10 if i % 2 else n1[i ] for i in range( len( n1 ) ) ]
    return sum(n1[1:]) * 9 % 10 == n%10

print(valid_credit_card(4111111111111111))
