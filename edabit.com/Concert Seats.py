# https://edabit.com/challenge/xbjDMxzpFcsAWKp97
def can_see_stage(seats):
    return all([x<y for i in range(len(seats)-1) for x,y in zip(seats[i],seats[i+1])])


print(can_see_stage([[1, 1, 2],[5, 2, 3],[6, 4, 4]]))