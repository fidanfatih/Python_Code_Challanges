"""
Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
"""
print(["FizzBuzz"*(not i%15) or "Fizz"*(not i%3) or "Buzz"*(not i%5) or i for i in range(1,101)])
