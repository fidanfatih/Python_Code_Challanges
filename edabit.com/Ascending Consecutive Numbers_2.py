# https://edabit.com/challenge/9iLhKgqZn5exBrmWm
from time import time

def ascending(txt):
    for i in range(1, len(txt)):
        numbers = int(txt[:i])
        new_numbers = str(numbers)
        if len(txt) % len(new_numbers):
            continue
        while len(new_numbers) < len(txt):
            numbers += 1
            new_numbers += str(numbers)
            if new_numbers == txt:
                return True
                break
    return False

t0=time()
print(ascending("500001500002500003500004500005"))
print(time()-t0)