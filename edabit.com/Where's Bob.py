# https://edabit.com/challenge/fDkAuAwR4PMWZwBKs
def find_bob(names):
    return names.index("Bob") if "Bob" in names else -1


print(find_bob ( [ "Jimmy" , "Layla" , "James" ] ))
print(find_bob ( [ "Jimmy" , "Layla" , "Bob" ] ))