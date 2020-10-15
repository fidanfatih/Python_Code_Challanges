# https://edabit.com/challenge/6vSZmN66xhMRDX8YT
def advanced_sort ( lst ) :
    return [ [ i ] * lst.count(i) for i in dict.fromkeys(lst) ]


def advanced_sort2 ( lst ) :
    return [ [ i ] * lst.count(i) for i in sorted(set(lst) , key=lst.index) ]


print(advanced_sort([ 7 , 'a' , 7 , 'b' , 10 , 'a' , 'b' , 'c' , '10' ]))
print(advanced_sort2([ 7 , 'a' , 7 , 'b' , 10 , 'a' , 'b' , 'c' , '10' ]))
