a=60
b=13
c=0
print(f"{'a=':>6}{a} =  {bin(a):>10}")          #   0011 1100  =60
print(f"{'b=':>6}{b} =  {bin(b):>10}")          #   0000 1101  =13

c=a&b
print(f"{'a&b=':>6}{c} =  {bin(c):>10} AND")          #   0000 1100  =12

c=a|b
print(f"{'a|b=':>6}{c} =  {bin(c):>10} OR")          #   0011 1101  =61

c=a^b
print(f"{'a^b=':>6}{c} =  {bin(c):>10} XOR")          #   0011 0001  =49

c=~a
print(f"{'-a=':>5}{c} = {bin(c):>11} COMPLEMENT")          #   1011 1101  =-61

c=a<<2
print(f"{'a<<2=':>5}{c} =  {bin(c):>10} LEFT SHIFT")          #   1111 0000  =240

c=a>>2
print(f"{'a>>2=':>6}{c} =  {bin(c):>10} RIGHT SHIFT")          #   0000 1111  =15

