# https://edabit.com/challenge/KETgxWCWtrk7oLM49
def tournament_scores(s):
    teams,score,goals,avar,output=set(),[],[],[],[]
    for i in s:
        item=i.split()
        teams.update(item[0],item[-1])
        score.append((item[0],3 if int(item[1])>int(item[-2]) else 1 if int(item[1])==int(item[-2]) else 0))
        score.append((item[-1],0 if int(item[1])>int(item[-2]) else 1 if int(item[1])==int(item[-2]) else 3))
        goals.append((item[0],int(item[1])))
        goals.append((item[-1],int(item[-2])))
        avar.append((item[0],int(item[1])-int(item[-2])))
        avar.append((item[-1],int(item[-2])-int(item[1])))
    teams=sorted(list(teams))

    for t in teams:
        x,y,z=[0,0,0]
        for s in score:
            if s[0]==t: x+=s[1]
        for g in goals:
            if g[0]==t: y+=g[1]
        for a in avar:
            if a[0]==t: z+=a[1]
        output.append([t,x,y,z])
    return sorted(output,key=lambda x:x[1:],reverse=True)

print(tournament_scores(["A 4 - 0 B", "C 2 - 1 D", "B 1 - 0 C", "D 3 - 2 A", "A 1 - 3 C", "B 2 - 1 D"]))
# [ [ "B", 7, 5, 3 ], [ "C", 5, 6, 2 ], [ "D", 3, 3, -2 ], [ "A", 1, 3, -3 ] ]

# Test.assert_equals(tournament_scores(["A 0 - 1 B", "C 2 - 0 D", "B 2 - 2 C", "D 3 - 1 A", "A 2 - 2 C", "B 2 - 0 D"]),
# [["B", 7, 5, 3], ["C", 5, 6, 2], ["D", 3, 3, -2], ["A", 1, 3, -3]], "Example #1");
# Test.assert_equals(tournament_scores(["A 0 - 0 B", "C 3 - 5 D", "B 1 - 0 C", "D 1 - 1 A", "A 2 - 2 C", "B 1 - 0 D"]),
# [["B", 7, 2, 2], ["D", 4, 6, 1], ["A", 3, 3, 0], ["C", 1, 5, -3]]);
# Test.assert_equals(tournament_scores(["A 4 - 0 B", "C 2 - 1 D", "B 1 - 0 C", "D 3 - 2 A", "A 1 - 3 C", "B 2 - 1 D"]),
# [["C", 6, 5, 2], ["B", 6, 3, -2], ["A", 3, 7, 1], ["D", 3, 5, -1]], "Example #2");
# Test.assert_equals(tournament_scores(["A 3 - 3 B", "C 0 - 6 D", "B 4 - 2 C", "D 0 - 1 A", "A 1 - 2 C", "B 2 - 1 D"]),
# [["B", 7, 9, 3], ["A", 4, 5, 0], ["D", 3, 7, 4], ["C", 3, 4, -7]]);
# Test.assert_equals(tournament_scores(["A 2 - 1 B", "C 3 - 0 D", "B 1 - 1 C", "D 1 - 0 A", "A 3 - 0 C", "B 2 - 4 D"]),
# [["A", 6, 5, 3], ["D", 6, 5, 0], ["C", 4, 4, 0], ["B", 1, 4, -3]], "Example #3");
# Test.assert_equals(tournament_scores(["A 0 - 1 B", "C 2 - 0 D", "B 0 - 0 C", "D 0 - 1 A", "A 0 - 2 C", "B 3 - 1 D"]),
# [["C", 7, 4, 4], ["B", 7, 4, 3], ["A", 3, 1, -2], ["D", 0, 1, -5]]);