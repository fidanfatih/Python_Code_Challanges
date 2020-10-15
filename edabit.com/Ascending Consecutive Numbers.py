# https://edabit.com/challenge/9iLhKgqZn5exBrmWm
def ascending ( txt ) :
    splitted=[split_txt(txt,step) for step in range(1,len(txt)//2+1)]
    # print(splitted)
    # print([is_iterate(txt) for txt in splitted])
    return any([is_iterate(txt) for txt in splitted])

def split_txt(txt,step):
    ch,s,splited='',step,[]
    for i in txt:
        ch+=i
        s-=1
        if not s:
            splited.append(ch)
            ch,s='',step
    if ch!='':
        splited.append(ch)
    print(splited)
    return splited

def is_iterate(txt):
    start,boolList=int(txt[0]),[]
    for i in txt[1:]:
        if int(i)!=start+1: return False
        else: start=int(i)
    return True


print(ascending("121314"))
