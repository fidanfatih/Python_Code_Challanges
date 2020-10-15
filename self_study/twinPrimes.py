def ebob(*n):
    for i in range(n[0],0,-1):
        if not(n[1]%i or n[0]%i): return i

nums=[int(input(f"Number{i+1}: ")) for i in range(2)]
print("NOT twin primes." if ebob(*sorted(nums))>1 else "twin primes")
