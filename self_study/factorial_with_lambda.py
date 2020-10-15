# def factorial(n):
#     return n<2 or n*factorial(n-1)
#
# print(factorial(int(input())))
#
factorial=lambda n:n<2 or n*factorial(n-1)
print(factorial(int(input())))