# https://edabit.com/challenge/frRRffQGSrPTknfxY
def digit_count(n):
    return int(''.join((str(str(n).count(i)) for i in str(n))))

print(digit_count(136116))  # 312332