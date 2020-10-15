# https://edabit.com/challenge/Bb9PaM4B87L39SdAo
def intersection_union(l1,l2):
    return [sorted(set(l1) & set(l2)),sorted(set(l1) | set(l2))]
    # return [sorted(list(set(l1).intersection(l2))),sorted(list(set(l1).union(l2)))]


print(intersection_union ( [ 1 , 3, 2, 4 , 4 ] , [ 4 , 5 , 9 ] ))