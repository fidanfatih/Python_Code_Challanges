# https://edabit.com/challenge/XPCqS7GYYouXg5ut9

# def simplify_sqrt(n1):
#     k=n1
#     for i in range(n1,0,-1):
#         if k**0.5==int(k**0.5) and n1%k==0:
#             return (int(k**0.5),n1//k)
#         k-=1


def simplify_sqrt(n):
	for b in range(1, n+1):
		a = (n/b)**.5
		if a.is_integer():
			return a, b

print(simplify_sqrt(72))
