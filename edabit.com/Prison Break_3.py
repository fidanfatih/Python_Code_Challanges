# https://edabit.com/challenge/SHdu4GwBQehhDm4xT

#jail=[1, 1, 0, 0, 0, 1, 0]  # 4
#jail= [1, 0, 0, 0, 0, 0, 0] # 2
#jail = [1, 1, 1, 0, 0, 0] #2

jail= [0, 0, 1, 1, 1, 0, 1]#6
jail = [ '1' if i else '0' for i in jail]
index , count = 0 , 0
while (True) :
    index = ''.join (jail).find ('1')
    if index == -1 :
        print (count)
        break
    jail = [ '0' if int(i) else '1' for i in jail[index:] ]
    count += 1