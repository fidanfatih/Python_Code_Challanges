{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
def square_dict(n):
    # return {i:i**2 for i in range(1,n1+1)}
    return dict((i+1,j**2) for i,j in enumerate(list(range(1,n+1))))


print(square_dict(15))