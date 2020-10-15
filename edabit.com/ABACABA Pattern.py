# https://edabit.com/challenge/FDzEFbNE2q3eKL8dm
def abacaba_pattern(n):
    ch,str=''.join([chr(65+i) for i in range(26)]),''
    for i in range(n): str+=ch[i]+str
    return str

print(abacaba_pattern(5))