import string
def print_rangoli(size):
    x=string.ascii_lowercase[:size]
    width=size+(size-1)
    width+=width-1
    print(x,width)
    for ii in range(1,size):
        print("-".join(x[-1:-ii:-1]+x[-ii:]).center(width, "-"))
    for i in range(size):
        print("-".join(x[size-1:i:-1]+x[i:]).center(width, "-"))

print_rangoli(int(input()))