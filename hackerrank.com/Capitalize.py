# https://www.hackerrank.com/challenges/capitalize/problem

# def solve(s):
#     for x in s.split():
#         for i in range(len(x)):
#             if x[i].isalpha():
#                 s = s.replace(x, x[:i]+x[i:].capitalize())
#     return s


def solve(s):
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s


s="1 w 2 r 3g"
print(solve(s))