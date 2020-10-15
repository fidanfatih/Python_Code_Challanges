# Longest Alternating Substring
# https://edabit.com/challenge/RB6iWFrCd6rXWH3vi

def longest_substring ( n ):
    txt=''
    for i in range(len(n)-1):
        if int(n[i])%2==int(n[i+1])%2:
            txt=txt[:-1]+n[i]+" "+n[i+1]
        else: txt=txt[:-1]+n[i]+n[i+1]
    return sorted(txt.split(),key=len,reverse=True)[0]



print(longest_substring ( "844929328912985315632725682153" ))  # 56327256